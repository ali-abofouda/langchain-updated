# الدرس الثالث: التحكم بالتدفق والتنفيذ المجمع عبر invoke و stream و batch

## 1. واجهة Runnable القياسية (LangChain Expression Language - LCEL)
تعتمد جميع المكونات في LangChain الحديثة على بروتوكول `Runnable`. يوفر هذا البروتوكول ثلاثة انماط متزامنة وثلاثة انماط غير متزامنة (Async):

| النمط المتزامن | النمط غير المتزامن (Async) | الوظيفة |
|---|---|---|
| `invoke` | `ainvoke` | تنفيذ استعلام مفرد واعطاء النتيجة كاملة |
| `stream` | `astream` | توليد الرد تدفقيا رمزا تلو الاخر (Token-by-Token) |
| `batch` | `abatch` | معالجة مصفوفة من المدخلات بالتوازي مع التحكم بالتزامن |

## 2. التنفيذ التدفقي (Streaming)
تعتبر ميزة التدفق حاسمة لتقليل زمن استجابة الرمز الاول (TTFT - Time To First Token) مما يمنح المستخدم انطباعا بالاستجابة الفورية:
```python
for chunk in model.stream("Write a short story about an autonomous robot."):
    print(chunk.content, end="", flush=True)
```
كل `chunk` عبارة عن كائن `AIMessageChunk`. يدعم LangChain دمج هذه المقاطع تلقائيا عبر عملية الجمع (`chunk1 + chunk2`).

## 3. المعالجة المجمعة والتحكم في التزامن (Batch with Concurrency)
عند معالجة الاف النصوص (مثل تصنيف المقالات او استخراج الكيانات)، يؤدي ارسال الطلبات الفردية الى بطء شديد، بينما ارسالها جميعا دفعة واحدة يؤدي الى حظر الحساب بسبب تجاوز معدل الطلبات (HTTP 429 Rate Limit Exceeded).
الحل المعياري في LangChain الحديثة هو استخدام `batch` مع تحديد `max_concurrency`:
```python
prompts = ["Prompt 1", "Prompt 2", "Prompt 3", "Prompt 4"]
results = model.batch(
    prompts,
    config={"max_concurrency": 2} # اتصالان متوازيان فقط في الوقت نفسه
)
```

## 4. اسئلة متوقعة في المقابلات الشخصية (Interview Questions)

### س1: ما الفرق بين invoke و stream و batch في بيئات الانتاج؟
**الاجابة النموذجية**:
- `invoke`: يُستخدم في الواجهات البرمجية التقليدية (REST APIs) وعمليات المعالجة الخلفية المستقلة حيث ينتظر النظام اكتمال النص بالكامل.
- `stream`: يُستخدم في تطبيقات المحادثة الفورية وتطبيقات الويب التفاعلية لعرض النص اثناء توليده لتحسين تجربة المستخدم وتقليل زمن الانتظار.
- `batch`: يُستخدم في معالجة البيانات الضخمة (ETL Pipelines / Data Processing) حيث ينظم تشغيل عشرات او مئات المهام بالتوازي مع ضمان احترام قيود الـ Rate Limits للمزود عبر `max_concurrency`.

### س2: كيف يعمل دمج مقاطع التدفق (AIMessageChunk concatenation) في LangChain؟
**الاجابة النموذجية**:
تطبق فئات `AIMessageChunk` مبدأ التحميل الزائد للعوامل (`__add__`)؛ فعند جمع مقطعين، يتم دمج النصوص في `content`، ودمج بيانات استدعاء الادوات المجزأة في `tool_call_chunks`، وتجميع بيانات التوكنات في `usage_metadata`.
