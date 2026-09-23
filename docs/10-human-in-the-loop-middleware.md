# الدرس العاشر: التدخل البشري والتحكم في العمليات الحساسة (Human-in-the-Loop Middleware)

## 1. حوكمة الوكلاء والعمليات الحساسة
عندما يُمنح الوكيل صلاحيات تنفيذية (مثل تنفيذ اوامر SQL، حذف ملفات، تحويل مالي، او ارسال بريد الكتروني)، لا يمكن الاعتماد كليا على استقلالية النموذج (Full Autonomy).
مفهوم التدخل البشري (Human-in-the-Loop - HITL) يضمن وجود نقطة تفتيش وموافقة صريحة من المشرف البشري قبل السماح للوكيل بتشغيل الاداة الحساسة.

## 2. معمارية `HumanInTheLoopMiddleware`
توفر `langchain.agents.middleware` الفئة `HumanInTheLoopMiddleware` التي تمكن المطور من تحديد الادوات المحمية عبر قاموس `interrupt_on`:
```python
from langchain.agents.middleware import HumanInTheLoopMiddleware

hitl_middleware = HumanInTheLoopMiddleware(
    interrupt_on={
        "execute_database_migration": True,
        "transfer_money": True
    },
    description_prefix="Approval Required for Sensitive Operation"
)

agent = create_agent(
    model=model,
    tools=[get_balance, transfer_money],
    middleware=[hitl_middleware]
)
```

## 3. مسار التدفق التنفيذي (Workflow Execution Flow)
1. يطلب المستخدم: "حول 5000 دولار الى الحساب رقم 9988".
2. يقرر النموذج استدعاء `transfer_money(amount=5000, account='9988')`.
3. تعترض البرمجية الوسيطة التنفيذ قبل تشغيل الدالة وتوقف الرسم البياني (Interrupt State).
4. يُعرض الطلب على لوحة تحكم المشرف البشري (Human Dashboard).
5. يملك المشرف ثلاثة خيارات:
   - **الموافقة (Approve)**: يستأنف الوكيل التنفيذ وينفذ التحويل.
   - **التعديل (Edit)**: تعديل المدخلات (مثلا تعديل المبلغ الى 3000) ثم المتابعة.
   - **الرفض (Reject)**: الغاء الاستدعاء واعادة رسالة توضيحية للوكيل بانه تم رفض العملية.

## 4. اسئلة متوقعة في المقابلات الشخصية (Interview Questions)

### س1: كيف تدعم معمارية LangGraph ميزة Interrupts واستئناف التنفيذ؟
**الاجابة النموذجية**:
تعتمد LangGraph على مخازن الحالات (Checkpointers مثل SQLite او Postgres Checkpointer). عندما يحدث Interrupt، يتم حفظ الحالة الراهنة للرسم البياني بالكامل في قاعدة البيانات مع معرف فريد للجلسة (`thread_id`). عند صدور موافقة المشرف البشري، يتم استرجاع الحالة من نفس النقطة ومتابعة التنفيذ دون اعادة تشغيل الخطوات السابقة.

### س2: ما اهمية توفير خيار تعديل المعاملات (Editing Tool Args) للمشرف البشري قبل التنفيذ؟
**الاجابة النموذجية**:
احيانا يستخرج النموذج اللغوي بيانات صحيحة بنسبة 90% ولكن مع خطأ طفيف في معامل واحد (مثل كتابة اسم المستخدم بحروف غير صحيحة). تتيح ميزة التعديل للمشرف تصحيح المعامل مباشرة دون الحاجة لرفض الطلب واجبار المستخدم على اعادة كتابة استفساره من البداية.
