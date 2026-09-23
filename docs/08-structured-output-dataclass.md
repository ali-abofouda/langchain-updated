# الدرس الثامن: الإخراج المهيكل باستخدام Python Dataclass

## 1. فئات البيانات القياسية (Python Dataclasses)
منذ الاصدار Python 3.7، تم توفير ديكوريتور `@dataclass` لتقليل كود التهيئة الروتيني للفئات (`__init__`, `__repr__`, `__eq__`). تدعم LangChain استخدام `@dataclass` كمخطط هيكلي في `with_structured_output`.

## 2. التطبيق العملي
```python
from dataclasses import dataclass, asdict

@dataclass
class InvoiceItem:
    """Information regarding a single line item on an invoice."""
    description: str
    quantity: int
    unit_price: float
    total_price: float

dataclass_llm = model.with_structured_output(InvoiceItem)
item = dataclass_llm.invoke("Purchased 4 mechanical keyboards at $75 each, totaling $300.")

print(item.description) # mechanical keyboards
print(item.total_price)  # 300.0

# تحويل الكائن الى قاموس بسهولة
dict_item = asdict(item)
```

## 3. الفروق الجوهرية بين الخيارات الثلاثة

| الخاصية | Pydantic | Dataclass | TypedDict |
|---|---|---|---|
| طريقة الوصول | `obj.attr` | `obj.attr` | `obj['key']` |
| التحقق الصارم في وقت التشغيل | نعم | لا (بدون مكتبات مساعدة) | لا |
| الاعتماديات | خارجية | مدمجة في بايثون | مدمجة في بايثون |
| دعم التحويل لقواميس | `model_dump()` | `asdict(obj)` | هو قاموس بالفعل |

## 4. اسئلة متوقعة في المقابلات الشخصية (Interview Questions)

### س1: هل تفضل استخدام Dataclass ام Pydantic في مشاريع الذكاء الاصطناعي الضخمة؟
**الاجابة النموذجية**:
في مشاريع الذكاء الاصطناعي الانتاجية (Enterprise Production)، يفضل Pydantic لانه يوفر Data Validation صارمة ويمنع دخول بيانات غير منطقية (مثل عمر سالب او بريد الكتروني غير صالح) الى قواعد البيانات. بينما يفضل Dataclass في السيناريوهات الداخلية البسيطة او عند الرغبة في الحفاظ على التوافق مع الشيفرات البرمجية القديمة التي تعتمد على Dataclasses.
