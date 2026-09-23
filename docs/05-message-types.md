# الدرس الخامس: منظومة الرسائل الحديثة وادارة سياق المحادثة (Messages & Trimming)

## 1. بنية الرسائل الاساسية في `langchain_core.messages`
تعتمد جميع المحادثات وتدفقات العمل في LangChain على فئات رسائل معيارية:
- `SystemMessage`: رسائل التوجيه الاساسية (Instructions & Guardrails).
- `HumanMessage`: استفسارات ومطالبات المستخدم.
- `AIMessage`: استجابات النموذج. تحتوي على خاصية `tool_calls` اذا قرر النموذج استدعاء ادوات.
- `ToolMessage`: تحمل نتيجة تنفيذ الاداة ويجب ان ترتبط بحقل `tool_call_id`.

## 2. دورة استدعاء الادوات عبر الرسائل
```text
User: "What is the weather in Cairo?"
  |
  v
HumanMessage(content="What is the weather in Cairo?")
  |
  v (Model Decision)
AIMessage(content="", tool_calls=[{'name': 'get_weather', 'args': {'city': 'Cairo'}, 'id': 'call_123'}])
  |
  v (Tool Execution)
ToolMessage(content="Sunny, 30 C", tool_call_id="call_123")
  |
  v (Model Synthesis)
AIMessage(content="The current weather in Cairo is sunny and 30 C.")
```

## 3. ادارة وتصغير سياق المحادثة عبر `trim_messages`
عند تشغيل وكيل في محادثات طويلة، يؤدي تراكم الرسائل الى نفاد نافذة السياق (Context Window). تقدم LangChain الدالة المتقدمة `trim_messages` للتعامل مع هذا التحدي:
```python
from langchain_core.messages import trim_messages

trimmed = trim_messages(
    messages,
    max_tokens=1000,
    strategy="last",
    token_counter=model, # عداد التوكنات الخاص بالنموذج
    include_system=True, # الحفاظ على رسالة النظام دائما في البداية
    start_on="human"     # التأكد من ان المحادثة تبدأ دائما برسالة مستخدم
)
```

## 4. اسئلة متوقعة في المقابلات الشخصية (Interview Questions)

### س1: لماذا يعتبر حقل tool_call_id ضروريا جدا داخل ToolMessage؟
**الاجابة النموذجية**:
في معمارية النماذج الحديثة الداعمة لاستدعاء الادوات المتوازي (Parallel Tool Calling)، قد يطلب النموذج استدعاء 3 ادوات في نفس رسالة `AIMessage`. لكي يطابق النموذج كل نتيجة بالاداة المناسبة لها بدقة، يتطلب بروتوكول المزود ربط كل `ToolMessage` بنفس المعرف الفريد `tool_call_id` الذي تم انشاؤه عند طلب الاستدعاء.

### س2: ما هي المخاطر التقنية لحذف الرسائل عشوائيا (Naive Slicing) بدلا من trim_messages؟
**الاجابة النموذجية**:
الحذف العشوائي (مثل `messages[-5:]`) قد يؤدي الى:
1. حذف رسالة النظام `SystemMessage` مما يفقد النموذج تعليماته وسياقه العام.
2. بقاء رسالة `ToolMessage` بدون رسالة `AIMessage` التي استدعتها او العكس، مما يؤدي الى رفض المزود للطلب ورمي خطأ `Invalid request: orphaned tool_call`.
تضمن `trim_messages` سلامة تسلسل المحادثة والحفاظ على ازواج استدعاءات الادوات كاملة.
