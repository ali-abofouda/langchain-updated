# LangChain Modern Architecture Repository (v1.x / v0.3+)

مرجع تطبيقي وتعليمي شامل لتحديثات مكتبة **LangChain** ومعمارية **LangGraph** الحديثة. تم تصميم هذا المستودع ليكون دليلاً عملياً ونظرياً وافياً لمهندسي الذكاء الاصطناعي (AI / LLM Engineers) يغطي كيفية بناء الوكلاء الاذكياء، تكامل النماذج الموحد، استدعاء الادوات، الإخراج المهيكل، وادارة السياق والبرمجيات الوسيطة.

---

## هيكل المستودع (Repository Structure)

```text
Langchain updated/
├── docs/                                  # مجلد التوثيق الخارجي بصيغة Markdown
│   ├── README.md                          # فهرس التوثيق وخريطة التعلم
│   ├── 01-creating-agents.md              # شرح دالة create_agent الحديثة
│   ├── 02-llm-model-integration.md        # شرح init_chat_model والتهيئة الموحدة
│   ├── 03-invoking-batch-streaming.md     # شرح التدفق والمعالجة المتوازية
│   ├── 04-implementing-tools.md           # بناء وتوثيق الادوات (@tool)
│   ├── 05-message-types.md                # منظومة الرسائل وتقليم السياق (trim_messages)
│   ├── 06-structured-output-pydantic.md   # الإخراج المهيكل عبر Pydantic V2
│   ├── 07-structured-output-typedict.md   # الإخراج المهيكل عبر TypedDict
│   ├── 08-structured-output-dataclass.md  # الإخراج المهيكل عبر Dataclass
│   ├── 09-summarization-middleware.md     # ادارة الذاكرة عبر SummarizationMiddleware
│   ├── 10-human-in-the-loop-middleware.md # التدخل البشري والامان (HITL Middleware)
│   └── interview-questions-guide.md       # دليل اسئلة المقابلات الفنية الشامل
├── updatedLangchain/                      # دفاتر العمل التطبيقية (Jupyter Notebooks)
│   ├── 01-creating-agents.ipynb
│   ├── 02-llm-model-integration.ipynb
│   ├── 03-invoking-batch-streaming.ipynb
│   ├── 04-implementing-tools.ipynb
│   ├── 05-message-types.ipynb
│   ├── 06-structured-output-pydantic.ipynb
│   ├── 07-structured-output-typedict.ipynb
│   ├── 08-structured-output-dataclass.ipynb
│   ├── 09-summarization-middleware.ipynb
│   └── 10-human-in-the-loop-middleware.ipynb
├── .env.example                           # نموذج المتغيرات البيئية
├── main.py                                # سكربت فحص سلامة وتكامل المستودع
├── pyproject.toml                         # ملف تكوين المشروع والحزم
└── requirements.txt                       # قائمة المتطلبات والاعتماديات
```

---

## فهرس الدروس التطبيقية (Interactive Notebooks)

| الدرس | الدفتر | الموضوع والتقنيات المستخدمة |
|---|---|---|
| 01 | `updatedLangchain/01-creating-agents.ipynb` | بناء الوكلاء باستخدام `create_agent` المعتمدة على `LangGraph` واستدعاء الادوات الاصلي. |
| 02 | `updatedLangchain/02-llm-model-integration.ipynb` | التهيئة الموحدة للنماذج عبر `init_chat_model` والتبديل المرن بين المزودين. |
| 03 | `updatedLangchain/03-invoking-batch-streaming.ipynb` | التحكم في تدفق النصوص ومعدل التزامن باستخدام `invoke`, `stream`, و `batch`. |
| 04 | `updatedLangchain/04-implementing-tools.ipynb` | انشاء وتوثيق الادوات البرمجية عبر `@tool` ومخططات Pydantic والتعامل مع الاخطاء. |
| 05 | `updatedLangchain/05-message-types.ipynb` | فهم دور `ToolMessage` و `AIMessage` واستخدام `trim_messages` لمنع تجاوز السياق. |
| 06 | `updatedLangchain/06-structured-output-pydantic.ipynb` | اجبار النماذج على اعادة مخرجات كائنات Pydantic صارمة عبر `with_structured_output`. |
| 07 | `updatedLangchain/07-structured-output-typedict.ipynb` | استخراج البيانات المهيكلة كقواميس بايثون نقية وسريعة باستخدام `TypedDict`. |
| 08 | `updatedLangchain/08-structured-output-dataclass.ipynb` | استخدام فئات البيانات المدمجة في بايثون `@dataclass` للإخراج المهيكل. |
| 09 | `updatedLangchain/09-summarization-middleware.ipynb` | تطبيق وسيط التلخيص التلقائي للمحادثات الطويلة لحماية نافذة السياق وتقليل التكلفة. |
| 10 | `updatedLangchain/10-human-in-the-loop-middleware.ipynb` | فرض موافقة المشرف البشري قبل تنفيذ العمليات الحساسة عبر البرمجية الوسيطة HITL. |

---

## دليل المقابلات الفنية (Interview Preparation)

يحتوي ملف `docs/interview-questions-guide.md` على اسئلة تقنية متعمقة تغطي:
- الفروق المعمارية بين LangChain القديمة (v0.1 / v0.2) والحديثة (v1.x / v0.3).
- لماذا تم استبدال `AgentExecutor` بـ `LangGraph`.
- معمارية بروتوكول Tool Calling وربط الرسائل بواسطة `tool_call_id`.
- المقارنة الفنية بين طرق الإخراج المهيكل (Pydantic vs TypedDict vs Dataclass).
- ادارة سياق الذاكرة والبرمجيات الوسيطة وتصميم انظمة Human-in-the-Loop.
- تحديات كودية عملية واجابات نموذجية.

---

## الاعداد والتشغيل (Setup & Execution)

### 1. المتطلبات الاساسية
- نظام تشغيل Windows / Linux / macOS.
- إصدار بايثون 3.11 أو 3.12.

### 2. تثبيت البيئة الافتراضية والاعتماديات
```powershell
# انشاء البيئة الافتراضية
python -m venv .venv

# تفعيل البيئة (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# تثبيت الحزم
pip install -r requirements.txt
```

### 3. ضبط مفاتيح الربط
قم بنسخ ملف `.env.example` الى `.env` واضف مفتاح Groq الخاص بك:
```env
GROQ_API_KEY=gsk_your_actual_key_here
```

### 4. فحص سلامة المستودع
يمكنك التحقق من توفر وسلامة كافة الملفات والبيئة عبر تشغيل:
```powershell
python main.py
```

### 5. فتح وتشغيل الدفاتر في Jupyter
```powershell
jupyter notebook updatedLangchain/
```
