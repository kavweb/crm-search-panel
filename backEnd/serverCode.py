from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# این بخش اجازه می‌ده فرانت‌اند (مثل React) بتونه با این API ارتباط بگیره
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # در حالت امن باید محدود بشه به دامنه خاص یا IP داخلی
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# این مسیر وقتی زده میشه (مثلاً http://localhost:8000/)
# فقط یک پیام ساده برمی‌گردونه تا بفهمیم سرور بالا هست
@app.get("/")
def read_root():
    return {"message": "سرور داخلی آماده است!"}

# مسیر جستجو: /search?q=چکش
@app.get("/search")
def search(q: str = Query(..., min_length=2)):
    # دیتای تستی - در آینده می‌تونی اینو از دیتابیس یا فایل اکسل بخونی
    fake_data = [
        {"title": "آچار", "desc": "ابزار برای باز و بسته کردن پیچ"},
        {"title": "پیچ‌گوشتی", "desc": "برای بستن پیچ‌های دوسو یا چهارسو"},
        {"title": "چکش", "desc": "ابزار کوبشی"},
    ]

    # فیلتر کردن داده‌ها بر اساس عبارت جستجو شده (q)
    results = [item for item in fake_data if q in item["title"] or q in item["desc"]]

    return {"results": results}



#powerdByAI