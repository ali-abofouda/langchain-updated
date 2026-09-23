# الدرس السادس: الإخراج المهيكل الصارم باستخدام Pydantic

## 1. المقدمة والمشكلة المعمارية
توليد النصوص الحرة بواسطة نماذج اللغة يجعل من الصعب دمجها في الانظمة البرمجية الانتاجية (مثل ادخال بيانات العملاء في قاعدة بيانات SQL). كان المطورون يلجأون الى تقنيات مثل `OutputFixingParser` او معالجة نصوص JSON عبر Regex، وهو حل هش وعرضة للاخطاء.

## 2. معمارية `with_structured_output` مع Pydantic
في LangChain الحديثة، تتيح الدالة `model.with_structured_output(Schema)` ارجاع كائنات Pydantic V2 مباشرة:
```python
from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    username: str = Field(description="Unique username")
    email: str = Field(description="Valid email address")
    age: int = Field(ge=18, le=120, description="User age, must be adult")

structured_llm = model.with_structured_output(UserProfile)
result = structured_llm.invoke("Create account for John Doe, email john@example.com, age 29")

print(type(result)) # <class 'UserProfile'>
print(result.username, result.age)
```

## 3. كيف تعمل الدالة داخليا؟
1. تحول كلاس Pydantic تلقائيا الى مواصفات JSON Schema.
2. ترسل المخطط الى النموذج عبر احد الاسلوبين (وفق قدرات المزود):
   - **Tool Calling Mode**: اجبار النموذج على استدعاء دالة وهمية وسائطها تطابق المخطط.
   - **JSON Mode / Strict Schema**: اجبار النموذج على اخراج نص JSON يطابق المخطط.
3. تقوم بالتحقق التلقائي من صحة البيانات (Validation) وتحويل النتيجة الى كائن Pydantic.

## 4. اسئلة متوقعة في المقابلات الشخصية (Interview Questions)

### س1: ما الفرق بين Tool Calling Mode و JSON Mode عند استخدام with_structured_output؟
**الاجابة النموذجية**:
- **Tool Calling Mode**: هو النمط الافتراضي والاكثر موثوقية لمعظم النماذج (GPT-4o, Claude 3.5). يجبر النموذج على تعبئة وسائط دالة، وهو ممتاز لدعم النماذج المتداخلة (Nested Schemas) والقوائم.
- **JSON Mode**: يوجه النموذج لانتاج مخرج JSON مباشر؛ ومع ذلك قد يتطلب تذكيرا صريحا في التوجيهات بالالتزام بالهيكل، بينما تفعل ميزة Structured Outputs الحديثة في OpenAI و Groq ذلك عبر قيود الجرامر الصارمة (Constrained Sampling).

### س2: ماذا يحدث اذا انتج النموذج حقلا يخالف شروط Pydantic (Validation Error)؟
**الاجابة النموذجية**:
يتم رمي استثناء `pydantic.ValidationError`. لمعالجة ذلك في الانتاج، يمكن تفعيل وسيط `include_raw=True` لفحص المخرج النصي الخام والخطأ البرمجي، او استخدام استراتيجيات اعادة المحاولة (Retry Chains) لتزويد النموذج برسالة الخطأ وتصحيح نفسه.
