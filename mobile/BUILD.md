# بناء تطبيق Pizza Hot للنشر

## ما تم تجهيزه

- `eas.json` بثلاثة مسارات:
  - `preview`: APK داخلي للاختبار.
  - `production`: Android App Bundle (`.aab`) للنشر على Google Play.
  - `production`: iOS archive/IPA للنشر على App Store Connect.
- معرّف Android: `com.pizzahot.balain`
- معرّف iOS: `com.pizzahot.balain`
- زيادة تلقائية لأرقام الإصدارات في الإنتاج.

## المتطلبات

1. حساب Expo/EAS.
2. مشروع Android في Google Play Console بالحزمة `com.pizzahot.balain`.
3. حساب Apple Developer وApp Store Connect.
4. قبول اتفاقيات المتجرين وإكمال بيانات التطبيق وسياسة الخصوصية.
5. إعداد شهادات التوقيع عبر EAS عند أول بناء.

## أوامر البناء

```bash
cd mobile
pnpm install
pnpm dlx eas-cli login
pnpm dlx eas-cli build:configure
```

لإنشاء APK اختبار:

```bash
pnpm dlx eas-cli build --platform android --profile preview
```

لإنشاء نسخة Android للنشر:

```bash
pnpm dlx eas-cli build --platform android --profile production
```

لإنشاء نسخة iOS للنشر:

```bash
pnpm dlx eas-cli build --platform ios --profile production
```

لبناء النظامين معًا:

```bash
pnpm dlx eas-cli build --platform all --profile production
```

## الإرسال للمتاجر

بعد نجاح البناء وربط حسابات المتاجر:

```bash
pnpm dlx eas-cli submit --platform android --profile production
pnpm dlx eas-cli submit --platform ios --profile production
```

## ملاحظة مهمة

لا يمكن إنشاء ملفات موقّعة نهائية أو رفعها للمتاجر دون حسابات Expo/EAS وشهادات Android/iOS. لا تضع كلمات المرور أو مفاتيح التوقيع في GitHub. استخدم EAS Secrets أو مدير أسرار آمن. البناء الحالي يستخدم WhatsApp والتخزين المحلي؛ قبل الإطلاق التجاري يجب إضافة Backend وقاعدة بيانات، سياسة خصوصية، وتسجيل طلبات حقيقي.
