# translation/views.py

from django.shortcuts import render
from django.conf import settings
import openai
from .forms import TranslationForm

# OpenAI APIキーを設定
openai.api_key = settings.OPENAI_API_KEY

def translate_text(text, target_language='ja'):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Translate the following text to {target_language}:"},
            {"role": "user", "content": text}
        ]
    )
    translation = response.choices[0].message.content.strip()
    return translation

def translate_view(request):
    translation = None
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            text_to_translate = form.cleaned_data['text_to_translate']
            translation = translate_text(text_to_translate)
    else:
        form = TranslationForm()
    
    return render(request, 'translation/translate.html', {'form': form, 'translation': translation})