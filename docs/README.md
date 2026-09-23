# دليل التحديثات الشامل لمكتبة LangChain الحديثة (v1.x / v0.3+)

## نظرة عامة
يقدم هذا المجلد توثيقا شاملا ومرجعيا لكافة المفاهيم والتحديثات الجوهرية التي طرأت على منصة ومكتبة LangChain. يركز التوثيق على التحول المعماري من السلاسل الخطية القديمة (Chains & AgentExecutor) الى منظومة الرسوم البيانية للحالات (LangGraph & State Graphs)، وتوحيد واجهات استدعاء النماذج وتوليد المخرجات المهيكلة والبرمجيات الوسيطة (Middleware).

---

## خريطة التعلم وجدول المحتويات

| الرقم | اسم الدفتر والدرس | الموضوع التقني الاساسي | الرابط |
|---|---|---|---|
| 01 | بناء الوكلاء (Creating Agents) | استبدال AgentExecutor بالدالة الحديثة create_agent | [01-creating-agents.md](01-creating-agents.md) |
| 02 | تكامل النماذج الموحد (Model Integration) | التهيئة الموحدة عبر init_chat_model | [02-llm-model-integration.md](02-llm-model-integration.md) |
| 03 | التدفق والتنفيذ المتوازي (Streaming & Batch) | واجهات invoke و stream و batch والتحكم بالتزامن | [03-invoking-batch-streaming.md](03-invoking-batch-streaming.md) |
| 04 | بناء وتوثيق الادوات (Implementing Tools) | الديكوريتور @tool ومخططات Pydantic والتعامل مع الاخطاء | [04-implementing-tools.md](04-implementing-tools.md) |
| 05 | منظومة الرسائل وادارة السياق (Messages & Trimming) | بنية الرسائل الحديثة وتقليم السياق عبر trim_messages | [05-message-types.md](05-message-types.md) |
| 06 | الإخراج المهيكل عبر Pydantic | التحقق الصارم من المخرجات عبر with_structured_output | [06-structured-output-pydantic.md](06-structured-output-pydantic.md) |
| 07 | الإخراج المهيكل عبر TypedDict | البديل الخفيف والمباشر لقواميس بايثون | [07-structured-output-typedict.md](07-structured-output-typedict.md) |
| 08 | الإخراج المهيكل عبر Dataclass | استخدام فئات البيانات القياسية في بايثون | [08-structured-output-dataclass.md](08-structured-output-dataclass.md) |
| 09 | برمجية وسيطة لتلخيص السياق (Summarization) | منع انفجار السياق عبر SummarizationMiddleware | [09-summarization-middleware.md](09-summarization-middleware.md) |
| 10 | التدخل البشري والامان (Human in the Loop) | تعليق العمليات الحساسة عبر HumanInTheLoopMiddleware | [10-human-in-the-loop-middleware.md](10-human-in-the-loop-middleware.md) |

---

## دليل المقابلات الفنية
- للاطلاع على بنك اسئلة المقابلات المتقدمة وإجاباتها النموذجية لمهندسي الذكاء الاصطناعي، يرجى مراجعة [دليل اسئلة الانترفيو الشامل](interview-questions-guide.md).
