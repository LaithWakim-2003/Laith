1- توصيف الحالة:
نبدأ باختيار المرحلة التي نريدها من خلال دخل المستخدم
نقوم بانشاء board جديد (و يتم تحديد عدد الأسطر والاعمدة عند انشاء الرقعة وتعريف list ثنائية)
وكل خانة من هذه الرقعة هي عبارة عن Normal_cell و وهي عبارة عن كلاس يحتوي على احداثيات كل خانة تحتوي ايضا علي attribute يدعى whitespace وهو قيمة بوليانية مسؤولة عن تحديد الخلايا الهدف(البيضاء)
يرث كلاس Normal_cell من كلاس cell بحيث يحتوي كلاس cell على اتريبيوت يدعى cell_type وهو مسؤول عن تحديد نوع الخلية (خلية فارغة)

2- فضاء الحالات:
يرث كلاس Normal_cell من كلاس cell بحيث يحتوي كلاس cell على اتريبيوت يدعى cell_type وهو مسؤول عن تحديد نوع الخلية (خلية فارغة)
يرث كلاس Magnet_Pos من كلاس cell بحيث يحتوي كلاس cell على اتريبيوت يدعى cell_type وهو مسؤول عن تحديد نوع الخلية (مغناطيس موجب)
يرث كلاس Magnet_Neg من كلاس cell بحيث يحتوي كلاس cell على اتريبيوت يدعى cell_type وهو مسؤول عن تحديد نوع الخلية (مغناطيس سالب)
يرث كلاس Iron من كلاس cell بحيث يحتوي كلاس cell على اتريبيوت يدعى cell_type وهو مسؤول عن تحديد نوع الخلية (قطعة حديدة)
يرث كلاس White_circle من كلاس cell بحيث يحتوي كلاس cell على اتريبيوت يدعى cell_type وهو مسؤول عن تحديد نوع الخلية (خلية بيضاء فارغة)
يرث كلاس Empty من كلاس cell و هو مسؤول عن تحديد جدار (خلية لا يمكن التحريك عليها يمكن انو توجد في وسط الرقعة)
حالة كل خانة (خلية فارغة - قطعة مغناطيسية موجبة - قطعة مغناطيسية سالبة - قطعة حديدية - خلية بيضاء فارغة)
يمكن الوصول لحالة الخسارة عند انتهاء عدد المحاولات

3- الحالة الابتدائية:
بعد انشاء ال board و توزيع ال Normal_cells نقوم باستدعاء توابع وكل تابع مسؤول عن عن وضع نوع الخلية من خلال انشاء object من الكلاسات التي ذكرت في فضاء الحالات وحسب ال object يتم تحديد ال cell_type ويتم تحديد ان كانت الخلية بيضاء ام لا ونميز حالتين:
الحالة الاولى: خلية بضاء فارغة ، ننشئ object من كلاس White_Circle ونضع اتريبيوت ال white_space قيمته true
الحالة الثانية: خلية بيضاء غير فارغة ، فحسب نوع الخلية نضع اتريبيوت ال white_space قيمته true
وتكون قيمته false في حال كانت الخلية غير بيضاء
4- العمليات والاجرائيات:
نقوم باختيار الخلية التي تحتوي على مغناطيس لتحريكه الى موقع جديد
وبعد تحريك المغناطيس نقوم بفحص نوعه ونميز حالتين:
اذا كان من النوع الموجب يتم تحريك القطع الحديدية في نفس السطر والعمود باتجاه المغناطيس
اذا كان من النوع السالب يتم تحريك القطع الحديدية في نفس السطر والعمود بالاتجاه المعاكس للمغنطيس
5- الحالة النهائية:
وبعد عمليات التحريك نقوم بفحص وضع الرقعة بحيث نمر على جميع الخلايا في حال كانت كل الخلايا البيضاء غير فارغة (تحتوي على مغناطيس او حديد) يتم الربح 
خوارزمية ال DFS:
نقوم بالتحقق من الرقعة في الحالة الابتدائية ونفحص ان كانت حالة رابحة ام لا ، في خال الربح يتم الخروج من الخوارزمية.
في حال عدم الربح:
تكون بنية التخزين stack بحيث ناخد كل الحالات ونضعها في ال stack ناخد الرقعة التي تكون في اعلى ال stack ونفحصها وبعد عملية الفحص نقوم بوضع الحلات التي تنتج عن هذه الحالة ونفحص الرقعة التي في اعلى ال stack ونستمر بحيث نقوم بزيادة العمق بكل فحص جديد حتى الوصول الى حالة رابحة.
نقوم بفحص الرقعة ان كانت مزارة ام لا عن طريق تحويل الرقعة الى string ونقوم بالمقارنة
في حال كانت مزارة نقوم بتجاهل هذه الرقعة
وان لم تكن مزارة نقوم باضافة الرقعة الى set تدعى visited ويتم تجاهلها في حال تم زيارة نفس شكل الرقعة مجددا
يمكن تحديد العمق الذي نريده عن طريق ال depth وعند الوصول لل depth المحدد لا نتغمق اكتر بالابناء بحيث نبدأ بفحص الاخوة
في كل حالة يمكننا تحريك المغناطيس اليها نقوم بانشاء رقعة جديدة (state) ولا يتم فحصها مباشرة لان هذه الرقع تكون الاخوة للرقعة التي يتم فحصها 

6-خوارزمية ال BFS:
تكون بنية التخزين queue ببحث نقوم بفحص جميع الابناء قبل الانتقال الى العمق الجديد
وتحديد الخلايا المزارة وحالة الربح هي نفس مبدأ ال DFS.