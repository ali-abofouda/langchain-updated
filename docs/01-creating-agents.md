# الدرس الاول: بناء الوكلاء الاذكياء عبر دالة create_agent الحديثة

## 1. المقدمة والتحول المعماري
في الاصدارات السابقة من LangChain (v0.0 وحتى v0.2 المبكرة)، كان المطورون يعتمدون على فئة `AgentExecutor` ودوال مثل `initialize_agent`. كان هذا النمط يعاني من قيود جوهرية:
- الاعتماد على التحليل النصي (Regex Parsing / ReAct parsing) لتخمين الاداة المراد استدعاؤها، مما ادى الى نسب فشل مرتفعة (Parsing Errors).
- صعوبة تخصيص دورة حياة الوكيل (Execution Loop) او حفظ واسترجاع الحالة (State Persistence).
- صعوبة تطبيق التفرعات الشرطية المعقدة او التراجع الزمني (Time Travel).

في التحديثات الحالية (LangChain 1.x و LangGraph):
- تم الاستغناء رسميا عن `AgentExecutor` واعتبارها مهملة (Deprecated).
- اصبحت الدالة الاساسية هي `create_agent` المدمجة مباشرة ضمن `langchain.agents` والتي تعيد كائنا من نوع `CompiledStateGraph`.
- يعتمد الوكيل كليا على استدعاء الادوات الاصلي (Native Tool Calling) الذي تدعمه نماذج مثل GPT-4o و Claude 3.5 و Llama 3 و Mistral.

## 2. كيفية عمل create_agent
تقوم الدالة بربط ثلاثة مكونات رئيسية:
1. **النموذج اللغوي (Model)**: يجب ان يكون نموذجا داعما لاستدعاء الدوال (Tool Calling Chat Model).
2. **قائمة الادوات (Tools)**: دوال بايثون معرفة وموثقة بدقة.
3. **التوجيهات الحاكمة (System Prompt)**: نص يحدد دور الوكيل وسياق عمله.

```python
from langchain_groq import ChatGroq
from langchain.agents import create_agent

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

def get_weather(city: str) -> str:
    """Get current weather conditions for a given city name."""
    return f"The weather in {city} is clear and pleasant."

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a polite assistant. Use tools when answering user questions."
)
```

## 3. دورة التنفيذ (Execution Cycle)
عند استدعاء الوكيل عبر `agent.invoke({"messages": [("user", "...")]})`:
1. يستقبل الوكيل رسالة المستخدم ويضيفها الى سجل الحالة (`messages`).
2. يرسل الوكيل السجل مع تعريف الادوات الى النموذج اللغوي.
3. يقرر النموذج ما اذا كان يحتاج الى اداة، ويعيد رسالة `AIMessage` تحتوي على حقل `tool_calls`.
4. يقوم محرك الرسم البياني (Graph Engine) تلقائيا بتوجيه الطلب الى عقدة تنفيذ الادوات (`tools node`).
5. يتم تشغيل الدالة والحصول على الناتج في رسالة من نوع `ToolMessage` تحمل نفس `tool_call_id`.
6. يعاد استدعاء النموذج اللغوي لتجميع النتيجة وصياغة الرد النهائي الموجه للمستخدم.

## 4. اسئلة متوقعة في المقابلات الشخصية (Interview Questions)

### س1: لماذا استبدلت LangChain فئة AgentExecutor بـ LangGraph ودالة create_agent؟
**الاجابة النموذجية**:
لان `AgentExecutor` كان عبارة عن صندوق اسود (Black Box) ينفذ حلقة تكرار ثابتة يصعب التحكم في تفاصيلها، وكان يعتمد على معالجة النصوص يدويًا للتعرف على الادوات مما يسبب اخطاء استخراج. اما في المعمارية الحديثة:
- الاعتماد على الرسوم البيانية للحالات (State Graphs) يوفر تحكما كاملا في كل خطوة وعقدة (Node).
- سهولة تطبيق التخزين المؤقت وحفظ الحالات (Checkpointers) لدعم المحادثات متعددة الجلسات.
- الدعم الاصلي لـ Native Tool Calling يضمن دقة عالية وتوافقا مباشرا مع بروتوكولات مزودي النماذج.

### س2: ما نوع الكائن الذي ترجعه دالة create_agent في LangChain 1.x؟
**الاجابة النموذجية**:
ترجع كائنا من نوع `CompiledStateGraph` وهو رسم بياني مجمع للحالة مبني على مكتبة LangGraph، ويوفر واجهة Runnable القياسية (`invoke`, `stream`, `batch`, `astream_events`).
