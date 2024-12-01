import pandas as pd
import re
from textblob import TextBlob
from nltk.corpus import stopwords
import nltk
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer


# Download stopwords
nltk.download('stopwords')

def analyze_multilingual_sentiment(text):
    negative_words = set([
        'مشكل', 'سيئ', 'خطأ', 'عطل', 'مشكلة', 'لا', 'ماشي', 'غالي','للأسف',
        'قبيح', 'ماعجبنيش', 'مانيش', 'مشي', 'خسارة', 'للاسف',
        'مش', 'ماكانش', 'معندكمش', 'صعيب', 'صعب', 'حرام', 'عوج','روطار',
        'مافاهمتش', 'باهض', 'مريض', 'زعفان', 'دمار', 'ضياع',
        'غلط', 'كارثة', 'رديء', 'معوج', 'مستحيل', 'ماكاينش', 'محال',
        'قاسح', 'ماينفعش', 'دون المستوى', 'معصب', 'مقرف', 'رداءة',
        'ضدي', 'موحش', 'قهر', 'كئيب', 'مظلم', 'مرهق', 'ثقيل',
        'مسكين', 'حزن', 'تعب', 'يأس', 'معكوس', 'مظلوم', 'جحيم',
        'مزيف', 'مؤلم', 'مخرب', 'مريض نفسي', 'مهمل', 'غير صالح',
        'سيئة', 'غلطة', 'غلطان', 'غلطان', 'غلطان', 'عالة', 'كسلان', 'بئيس', 'نهار سود', 'غشاش', 'حرام عليكم'
    ])

    # Positive and Negative word lists for Arabic
    positive_words = set([
        'شكرا', 'ممتاز', 'جيد', 'رائع', 'حسن', 'بارك', 'نعم', 'مليح',
        'باهي', 'عجبني', 'زين', 'برافو', 'تمام', 'صح', 'مبروك',
        'نشكر', 'متشكر', 'الله', 'الحمد', 'جميل', 'كويس', 'خير',
        'ربي يعاون', 'يعطيك الصحة', 'صحيحة', 'ماشاءالله', 'هايل',
        'بهي', 'قوي', 'فرحان', 'شيء مليح', 'كلش مليح', 'تبارك الله',
        'نشالله', 'على خير', 'ساهل', 'قريب', 'محترم', 'طيبة',
        'بالعافية', 'فوق الممتاز', 'روعة', 'سعيد', 'لطيف', 'لطافة',
        'تهلا', 'زاهي', 'بوركت', 'عظيم', 'يا سلام', 'مدهش', 'راقي',
        'مليحة', 'بالزاف مليح', 'نشكر الله', 'خاطيني', 'مرتاح', 
        'مافيش خير', 'بالمعقول', 'زاهية', 'خير من الخير', 'مغبوط', 
        'تهاني', 'أفضل', 'شيء زين', 'جزاك الله خير', 'في أمان الله'
    ])
    
    # Define stopwords for Arabic
    arabic_stopwords = set(stopwords.words('arabic'))
    
    """
    Analyze the sentiment of a given text (Arabic or French).
    Returns: ("language", "sentiment").
    """
    if pd.isna(text) or not text.strip():
        return "unknown", "neutral"

    # Step 1: Clean the text
    text = str(text)  # Ensure it's a string
    text = re.sub(r'http\S+|www.\S+', '', text)  # Remove URLs
    text = re.sub(r'[^\u0600-\u06FFa-zA-ZàâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ\s]', ' ', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace

    # Step 2: Detect language
    arabic_count = len(re.findall(r'[\u0600-\u06FF]', text))
    french_count = len(re.findall(r'[a-zA-ZàâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ]', text))
    
    if arabic_count > french_count:
        language = "arabic"
    elif french_count > arabic_count:
        language = "french"
    else:
        language = "unknown"

    # Step 3: Sentiment Analysis
    sentiment = "neutral"  # Default sentiment
    if language == "french":
        # Using TextBlob with French support
        tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        sentiment_value = tb(text).sentiment[0]
        
        # Classify sentiment based on polarity
        if sentiment_value > 0:
            sentiment = "positive"
        elif sentiment_value < 0:
            sentiment = "negative"

    elif language == "arabic":
        # Analyze Arabic sentiment based on predefined word lists
        words = set(text.lower().split())
        words = words - arabic_stopwords  # Remove stopwords
        positive_count = sum(1 for word in words if word in positive_words)
        negative_count = sum(1 for word in words if word in negative_words)

        if positive_count > negative_count:
            sentiment = "positive"
        elif negative_count > positive_count:
            sentiment = "negative"

    return language, sentiment


# Example test cases
text_french = "C'est une journée magnifique, je suis très heureux."
text_arabic = "شكرا لكم، كان العمل ممتاز"

print(analyze_multilingual_sentiment(text_french))  # Output: ("french", "positive")
print(analyze_multilingual_sentiment(text_arabic))  # Output: ("arabic", "positive")
