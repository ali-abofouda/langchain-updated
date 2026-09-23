# الدرس الرابع: بناء وتوثيق الادوات البرمجية (Implementing Tools)

## 1. المقدمة والمفاهيم الجوهرية
الاداة (Tool) هي دالة برمجية يمنحها المطور للوكيل الذكي للتفاعل مع العالم الخارجي (قواعد البيانات، واجهات API، الحسابات الرياضية). في المعمارية الحديثة، يتم بناء الادوات باستخدام الديكوريتور `@tool` من `langchain_core.tools`.

## 2. تشريح الاداة الاحترافية
لكي يستطيع النموذج اللغوي استدعاء الاداة بدقة، يجب توفر:
1. **اسم وصفي واضح**: يعبر بدقة عن وظيفة الاداة.
2. **نص توثيقي شامل (Docstring)**: يقرأه النموذج لفهم متى ولماذا يستخدم الاداة.
3. **تحديد انواع المدخلات والمخرجات (Type Hints)**.

```python
from langchain_core.tools import tool

@tool
def calculate_vat(subtotal: float, tax_rate: float = 0.15) -> str:
    """Calculate VAT tax amount and total invoice price.
    
    Args:
        subtotal: The net amount before taxes.
        tax_rate: The tax rate fraction (default is 0.15 for 15%).
    """
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    return f"Net: ${subtotal:.2f}, Tax: ${tax_amount:.2f}, Total: ${total:.2f}"
```

## 3. استخدام مخططات Pydantic المتقدمة (Args Schema)
عندما تحتوي الاداة على معاملات معقدة او شروط تحقق محددة، نستخدم خاصية `args_schema`:
```python
from pydantic import BaseModel, Field

class OrderFilterSchema(BaseModel):
    status: str = Field(description="Order status: pending, completed, or cancelled")
    min_amount: float = Field(ge=0, description="Minimum order total amount")

@tool(args_schema=OrderFilterSchema)
def filter_orders(status: str, min_amount: float) -> str:
    """Query database for orders matching status and threshold amount."""
    # Implementation logic here
    return f"Retrieved orders matching status '{status}' above ${min_amount}."
```

## 4. ربط الادوات بالنماذج (Tool Binding)
بدلا من كتابة التوجيهات يدويا، نستخدم `model.bind_tools([tools])`. تقوم هذه الدالة بتحويل دوال بايثون تلقائيا الى مواصفات JSON Schema مطابقة لمعايير OpenAI / Anthropic / Groq Function Calling.

## 5. اسئلة متوقعة في المقابلات الشخصية (Interview Questions)

### س1: ما الدور الفعلي لنص التوثيق (Docstring) داخل الادوات في LangChain؟
**الاجابة النموذجية**:
نص التوثيق ليس مجرد تعليق لقراءة المطورين؛ بل تقوم LangChain باستخراجه وتحويله الى حقل `description` داخل مواصفات JSON Schema التي ترسل الى النموذج اللغوي. يقرر النموذج اللغوي استدعاء الاداة من عدمه بناء على مطابقة استفسار المستخدم لهذا الوصف.

### س2: كيف تتعامل مع اخطاء تنفيذ الادوات (Tool Exceptions) حتى لا يتعطل الوكيل؟
**الاجابة النموذجية**:
يمكن استخدام الوسيط `handle_tool_error=True` او تمرير دالة مخصصة لمعالجة الاستثناءات داخل ديكوريتور `@tool`. هذا يضمن انه عند حدوث خطأ برمجي (مثل فشل الاتصال بقاعدة البيانات)، يتم تغليف رسالة الخطأ كناتج نصي يعاد الى النموذج في رسالة `ToolMessage`، مما يتيح للنموذج فهم سبب الفشل واعلام المستخدم او محاولة اصلاح المدخلات.
