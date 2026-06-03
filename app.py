import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="مرشد الباحة الذكي",
    layout="wide"
)
st.markdown("""
<style>

html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
}

</style>
""", unsafe_allow_html=True)
# قراءة قاعدة البيانات
df = pd.read_excel("data/places_smart.xlsx")
df["SearchText"] = (

df["Name"].fillna("") + " " +

df["Tags"].fillna("") + " " +

df["Reason"].fillna("")

)
# القائمة الجانبية
page = st.sidebar.selectbox(
    "القائمة",
    [
        "مرشد الباحة الذكي",
        "عن المشروع",
        "فريق العمل"
    ]
)

# =========================
# صفحة نبذة عن المشروع
# =========================
if page == "عن المشروع":

    st.title("نبذة عن المشروع")

    st.image(
        "images/project_overview.jpeg",
        use_container_width=True
    )

    st.markdown("""
    <div dir="rtl" style="
    text-align:right;
    line-height:2.2;
    font-size:20px;
    background-color:#eef5ff;
    padding:30px;
    border-radius:15px;
    ">

    <h2>الهدف من النظام</h2>

    يهدف النظام إلى:

    • تسهيل عملية التخطيط للرحلات السياحية داخل منطقة الباحة.<br>

    • مساعدة الزوار على اكتشاف الأماكن المناسبة لهم.<br>

    • توفير توصيات سياحية ذكية ومخصصة لكل فئة من الزوار.<br>

    • دعم السياحة المحلية وإبراز معالم منطقة الباحة.<br>

    • تحسين تجربة الزائر وتقليل الوقت والجهد.<br><br>

    <h2>كيف يعمل النظام؟</h2>

    ١- يحدد المستخدم نوع الرحلة المناسبة له.<br>

    ٢- يختار اهتماماته وتفضيلاته السياحية.<br>

    ٣- يبحث النظام داخل قاعدة البيانات عن الأماكن المناسبة.<br>

    ٤- يطابق النتائج مع نوع الرحلة والاهتمامات المختارة.<br>

    ٥- ينشئ خطة زيارة ذكية تتضمن أفضل الوجهات المقترحة.<br><br>

    <h2>مميزات النظام</h2>

    ⭐ فهم اهتمامات المستخدم وتخصيص التوصيات.<br>

    ⭐ اقتراح أماكن سياحية ومطاعم ومقاهي مناسبة.<br>

    ⭐ إنشاء خطة زيارة متكاملة تلقائياً.<br>

    ⭐ عرض أسباب ترشيح الأماكن لزيادة الشفافية.<br>

    ⭐ سهولة الاستخدام لجميع فئات الزوار.<br>

    ⭐ إمكانية التوسع وربط النظام بخدمات الخرائط مستقبلاً.<br><br>

    <h2>النتائج المتوقعة</h2>

    ✔ زيادة الوعي بالمواقع السياحية في منطقة الباحة.<br>

    ✔ مساعدة الزوار في اختيار أفضل الأماكن المناسبة لهم.<br>

    ✔ تحسين تجربة التخطيط للرحلات السياحية.<br>

    ✔ دعم السياحة المحلية وإبراز الوجهات المميزة.<br>

    ✔ تقديم تجربة سياحية ذكية وتفاعلية للمستخدم.<br>

    </div>
    """, unsafe_allow_html=True)

# =========================
# صفحة فريق العمل
# =========================
elif page == "فريق العمل":

    st.title("فريق العمل")

    st.success("""
ألين أحمد

كوثر سالم

درر محمد
""")

# =========================
# الصفحة الرئيسية
# =========================
else:

    st.image("images/cover.jpg", use_container_width=True)

    st.markdown(
        """
        <h2 style='text-align:center;color:#0B5D3B'>
        مشروع مشارك في هاكثون تعليم الباحة لطلاب التعليم العام
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h1 style='text-align:center'>
        🤖 مرشد الباحة الذكي
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.info(
            """
        💡 يمكنك استخدام أي طريقة تناسبك:
        • اختر نوع الزائر للحصول على أماكن مناسبة للفئة المستهدفة.
         و اختر الاهتمامات لتخصيص النتائج حسب رغبتك
        • أو اكتب وصفاً حراً للرحلة وسيستخدم النظام الذكاء الاصطناعي لتحليل طلبك واقتراح أفضل الوجهات.
        """
    )
    search_mode = st.radio(
    "اختر طريقة إنشاء الخطة",
    [
    "بحث بالتفضيلات",
    "بحث ذكي بالذكاء الاصطناعي"
    ]
    )

    if search_mode == "بحث بالتفضيلات":

        visitor_type = st.selectbox(
            "نوع الزائر",
            [
                "عائلة مع أطفال",
                "شباب فقط",
                "كبار السن"
            ]
        )

        if visitor_type == "عائلة مع أطفال":

            preferences = st.multiselect(
                "اختر اهتمامات الرحلة",
                [
                    "أماكن طبيعية",
                    "حدائق",
                    "مطاعم عائلية",
                    "مقاهي عائلية",
                    "أماكن ترفيهية"
                ]
            )

        elif visitor_type == "شباب فقط":

            preferences = st.multiselect(
                "اختر اهتمامات الرحلة",
                [
                    "تصوير",
                    "أماكن تراثية",
                    "مقاهي",
                    "مطاعم",
                    "إطلالات طبيعية"
                ]
            )
        else:

            preferences = st.multiselect(
                "اختر اهتمامات الرحلة",
                [
                    "أماكن هادئة",
                    "جلسات مريحة",
                    "إطلالات طبيعية",
                    "مطاعم",
                    "مقاهي"
                ]
            )

    else:

        user_request = st.text_area( 
            "صف رحلتك بالكلمات التي تريدها", 
            height=100, 
            placeholder="مثال: أريد مكاناً طبيعياً هادئاً مناسباً لكبار السن"
        ) 
        st.caption( 
            "يستخدم النظام TF-IDF و Cosine Similarity لتحليل الوصف واقتراح أفضل الوجهات." 
        )
    if st.button("إنشاء خطة ذكية"):

        results = df.copy()

        # =====================
        # البحث بالتفضيلات
        # =====================

        if search_mode == "بحث بالتفضيلات":

            if visitor_type == "عائلة مع أطفال":

                results = results[
                    results["Category"].str.contains(
                        "عائلة|الجميع",
                        na=False
                    )
                ]

            elif visitor_type == "شباب فقط":

                results = results[
                    results["Category"].str.contains(
                        "شباب|الجميع",
                        na=False
                    )
                ]

            else:

                results = results[
                    results["Category"].str.contains(
                        "كبار|الجميع",
                        na=False
                    )
                ]

            interest_mapping = {

                "أماكن طبيعية": ["طبيعة", "إطلالة"],
                "حدائق": ["حديقة"],
                "مطاعم عائلية": ["مطعم", "عائلات"],
                "مقاهي عائلية": ["كوفي", "عائلات"],
                "أماكن ترفيهية": ["ترفيه"],

                "تصوير": ["تصوير"],
                "أماكن تراثية": ["تراث"],
                "مقاهي": ["كوفي"],
                "مطاعم": ["مطعم"],
                "إطلالات طبيعية": ["إطلالة", "طبيعة"],

                "أماكن هادئة": ["جلسات", "استرخاء"],
                "جلسات مريحة": ["جلسات", "استرخاء"]
            }

            results["Score"] = 0

            for pref in preferences:

                keywords = interest_mapping.get(
                    pref,
                    []
                )

                for keyword in keywords:

                    results.loc[
                        results["Tags"].str.contains(
                            keyword,
                            case=False,
                            na=False
                        ),
                        "Score"
                    ] += 1

            results = results[
                results["Score"] > 0
            ]

            if len(results) == 0:

                st.error(
                    "لم يتم العثور على نتائج مناسبة"
                )

                st.stop()

            region_scores = (
                results.groupby("Region")["Score"]
                .sum()
                .sort_values(
                    ascending=False
                )
            )

            selected_region = (
                region_scores.index[0]
            )

            results = results[
                results["Region"] == selected_region
            ]

            results = results.sort_values(
                by="Score",
                ascending=False
            )


    # =====================
    # البحث الذكي
    # =====================

        else:

            if user_request.strip() == "":

                st.warning(
                    "يرجى وصف الرحلة المطلوبة أولاً"
                )

                st.stop()

            results["SearchText"] = (
                results["Name"].fillna("") + " " +
                results["Category"].fillna("") + " " +
                results["Type"].fillna("") + " " +
                results["Tags"].fillna("") + " " +
                results["Reason"].fillna("")
            )

            corpus = results["SearchText"].tolist()

            vectorizer = TfidfVectorizer(
                analyzer="char_wb",
                ngram_range=(3, 5)
            )

            tfidf_matrix = vectorizer.fit_transform(
                corpus + [user_request]
            )

            user_vector = tfidf_matrix[-1]

            place_vectors = tfidf_matrix[:-1]

            similarities = cosine_similarity(
                user_vector,
                place_vectors
            ).flatten()

            results["AI_Score"] = similarities

            results = results[
                results["AI_Score"] > 0
            ]

            if len(results) == 0:

                st.error(
                    "لم يتم العثور على نتائج مناسبة"
                )

                st.stop()

            region_scores = (
                results.groupby("Region")["AI_Score"]
                .sum()
                .sort_values(
                    ascending=False
                )
            )

            selected_region = (
                region_scores.index[0]
            )

            results = results[
                results["Region"] == selected_region
            ]

            results = results.sort_values(
                by="AI_Score",
                ascending=False
            )

        st.success(
            f"تم إنشاء خطة ذكية في منطقة {selected_region}"
        )

        st.info(
            f"📍 تم اختيار منطقة {selected_region} لأنها الأكثر توافقاً مع طلبك."
        )

        st.subheader(
            "الخطة المقترحة"
        )

        tourist_places = results[
            results["Type"] == "سياحي"
        ]

        restaurants = results[
            results["Type"] == "مطعم"
        ]

        cafes = results[
            results["Type"] == "مقهى"
        ]

        plan_rows = []

        if len(tourist_places) > 0:
            plan_rows.append(
                tourist_places.iloc[0]
            )

        if len(restaurants) > 0:
            plan_rows.append(
                restaurants.iloc[0]
            )

        if len(cafes) > 0:
            plan_rows.append(
                cafes.iloc[0]
            )

        remaining = tourist_places.iloc[1:]

        for _, row in remaining.iterrows():

            if len(plan_rows) < 5:

                plan_rows.append(
                    row
                )

        selected_places = pd.DataFrame(
            plan_rows
        )

        times = [
            "09:00 صباحاً",
            "12:30 ظهراً",
            "03:30 عصراً",
            "05:30 مساءً",
            "07:30 مساءً"
        ]

        for i, (_, row) in enumerate(
            selected_places.iterrows()
        ):

            if i < len(times):

                st.write(
                    f"{times[i]} — {row['Name']}"
                )

        st.markdown("---")

        st.subheader(
            "صور الأماكن"
        )

        cols = st.columns(2)

        for index, (_, row) in enumerate(
            selected_places.iterrows()
        ):

            with cols[index % 2]:

                try:

                    st.image(
                        f"images/{row['Image']}",
                        use_container_width=True
                    )

                except:

                    st.warning(
                        f"الصورة غير موجودة: {row['Image']}"
                    )

                st.markdown(
                    f"<h4 style='text-align:center'>{row['Name']}</h4>",
                    unsafe_allow_html=True
                )

                st.caption(
                    row["Address"]
                )

                if pd.notna(
                    row["Maps"]
                ):

                    st.link_button(
                        "📍 فتح الموقع على الخريطة",
                        row["Maps"]
                    )