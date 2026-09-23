# الدرس السابع: الإخراج المهيكل باستخدام TypedDict

## 1. المقدمة والبديل الخفيف
على الرغم من قوة Pydantic، الا ان بعض الانظمة تفضل تجنب الاعتماديات الاضافية او تحتاج الى التعامل المباشر مع قواميس بايثون القياسية (`dict`). تدعم دالة `with_structured_output` فئات `TypedDict` الاصلية في بايثون.

## 2. بناء المخطط عبر TypedDict و Annotated
نستخدم `typing.Annotated` لتوفير الوصف الذي يقرأه النموذج اللغوي:
```python
from typing import TypedDict, Annotated, List

class VulnerabilityReport(TypedDict):
    cve_id: Annotated[str, "The Common Vulnerabilities and Exposures identifier"]
    severity: Annotated[str, "Severity: LOW, MEDIUM, HIGH, or CRITICAL"]
    cvss_score: Annotated[float, "Numerical score from 0.0 to 10.0"]
    remediation_steps: Annotated[List[str], "Recommended mitigation actions"]

typed_model = model.with_structured_output(VulnerabilityReport)
report = typed_model.invoke("Report on CVE-2024-1234: critical flaw in authentication with score 9.8...")
```

## 3. مقارنة بين Pydantic و TypedDict

| المعيار | Pydantic V2 | TypedDict |
|---|---|---|
| الحزم والاعتماديات | يتطلب تثبيت `pydantic` | مدمج في مكتبة بايثون القياسية |
| نوع المخرج | كائن فئة (`instance.field`) | قاموس بايثون نقي (`dict['key']`) |
| التحقق من القيود (Constraints) | يدعم (`ge`, `le`, regex, custom validators) | لا يدعم التحقق اثناء وقت التشغيل (Type hints only) |
| الاداء وزمن التنفيذ | سريع ولكن به طبقة معالجة وتحقق | اسرع جدا لانه لا يقوم بفحص القيود المعقدة |

## 4. اسئلة متوقعة في المقابلات الشخصية (Interview Questions)

### س1: متى تفضل استخدام TypedDict بدلا من Pydantic مع with_structured_output؟
**الاجابة النموذجية**:
افضل `TypedDict` عندما:
1. يكون المشروع مصمما ليعمل بدون اي تبعيات خارجية اضافية (Lightweight architecture).
2. تكون البيانات المستخرجة متجهة مباشرة الى طبقة serialization (مثل JSON API response) ولا تحتاج الى دوال مخصصة او منطق عمل (Business Logic methods).
3. تكون سرعة المعالجة حرجة جدا والبيانات بسيطة ولا تتطلب قيود تحقق مشروطة.
