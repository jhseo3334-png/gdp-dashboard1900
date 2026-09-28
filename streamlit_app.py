import html

import streamlit as st


st.set_page_config(
    page_title='서지형 | 나를 소개해요',
    page_icon='👋',
    layout='wide',
)

PROFILE_DEFAULTS = {
    'name': '서지형',
    'nickname': '',
    'gender': '여성',
    'location': '서울',
    'intro': '서울에서 걷는 시간을 즐기고, 떡볶이와 강아지를 좋아하는 서지형입니다.',
    'favorite_color': '선택 안 함',
    'hobby': '걷기',
    'food': '떡볶이',
    'animal': '강아지',
    'music': '',
    'fun_fact': '',
    'weekend': '',
    'quote': '',
    'link': '',
}

for key, default in PROFILE_DEFAULTS.items():
    st.session_state.setdefault(key, default)

COLOR_OPTIONS = {
    '선택 안 함': ('🐾', '#e8efe9'),
    '초록': ('🌿', '#dceee3'),
    '파랑': ('🌊', '#dcebf4'),
    '노랑': ('☀️', '#f5edc9'),
    '분홍': ('🌸', '#f5e1e8'),
    '보라': ('🔮', '#eae3f3'),
    '주황': ('🍊', '#f5e5d5'),
}
DOG_IMAGE_URL = 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?auto=format&fit=crop&w=1200&q=85'

st.markdown(
    '''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #20312f;
        --muted: #687774;
        --green: #3f806b;
        --line: #e1e9e3;
        --canvas: #f5f7f2;
        --accent: #d5bd68;
    }
    .stApp {
        background: linear-gradient(135deg, #f5f7f2 0%, #edf4ef 58%, #f8f5eb 100%);
        color: var(--ink);
        font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stMainBlockContainer"] { max-width: 1120px; padding-top: 2.2rem; }
    h1, h2, h3, p, label, button, input, textarea, [data-testid="stMarkdownContainer"] {
        font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    }
    .eyebrow { color: var(--green); font-size: .76rem; font-weight: 700; letter-spacing: .08em; margin-bottom: .7rem; }
    .hero-title { color: var(--ink); font-size: 2.8rem; font-weight: 800; line-height: 1.2; margin: 0; }
    .hero-copy { animation: rise-in .55s ease-out both; padding: 2.5rem 0 1.8rem; }
    .hero-intro { color: #52645e; font-size: 1.05rem; line-height: 1.8; margin-top: 1rem; max-width: 34rem; }
    .hero-note { color: var(--green); font-size: .88rem; font-weight: 600; margin-top: 1.4rem; }
    div[data-testid="stImage"] { animation: rise-in .7s ease-out both; }
    div[data-testid="stImage"] img { border-radius: 10px; }
    .section-heading { color: var(--ink); font-size: 1.12rem; font-weight: 700; margin: 1.7rem 0 .6rem; }
    .fact { border-top: 1px solid var(--line); padding: .85rem .15rem .75rem; }
    .fact-label { color: var(--muted); font-size: .76rem; margin-bottom: .32rem; }
    .fact-value { color: var(--ink); font-size: 1rem; font-weight: 650; overflow-wrap: anywhere; }
    .stExpander { border-color: var(--line); border-radius: 8px; }
    div[data-testid="stForm"] { border: 0; padding: .8rem .2rem .2rem; }
    div[data-testid="stForm"] label { color: #455852; }
    .stButton button, .stDownloadButton button { border-radius: 6px; font-weight: 600; }
    @keyframes rise-in { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    @media (max-width: 640px) {
        [data-testid="stMainBlockContainer"] { padding: 1rem 1rem 2rem; }
        .hero-copy { padding: .6rem 0 1.2rem; }
        .hero-title { font-size: 2.15rem; }
        .hero-intro { font-size: .98rem; }
    }
    </style>
    ''',
    unsafe_allow_html=True,
)

name = st.session_state['name'].strip() or '서지형'
intro = st.session_state['intro'].strip()
nickname = st.session_state['nickname'].strip()
location = st.session_state['location'].strip()
gender = st.session_state['gender'].strip()
favorite_color = st.session_state['favorite_color']
color_emoji, color_hex = COLOR_OPTIONS.get(favorite_color, COLOR_OPTIONS['선택 안 함'])

hero_left, hero_right = st.columns([1.05, 0.95], gap='large', vertical_alignment='center')
with hero_left:
    st.markdown(
        f'<div class="hero-copy">'
        f'<div class="eyebrow">A LITTLE ABOUT ME</div>'
        f'<h1 class="hero-title">안녕하세요,<br>{html.escape(name)}입니다</h1>'
        f'<div class="hero-intro">{html.escape(intro)}</div>'
        f'<div class="hero-note">📍 {html.escape(location or "서울")}에서 천천히, 즐겁게</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
with hero_right:
    st.image(DOG_IMAGE_URL, caption='산책길에서 만난 사랑스러운 친구들', width='stretch')

st.markdown('<div class="section-heading">지형의 취향과 일상</div>', unsafe_allow_html=True)
facts = [
    ('성별', gender),
    ('사는 곳', location),
    ('좋아하는 음식', st.session_state['food'].strip()),
    ('취미', st.session_state['hobby'].strip()),
    ('가장 좋아하는 동물', st.session_state['animal'].strip()),
]
if favorite_color != '선택 안 함':
    facts.append(('좋아하는 컬러', f'{color_emoji} {favorite_color}'))
if nickname:
    facts.append(('별명', nickname))
facts.extend([
    ('요즘 듣는 음악', st.session_state['music'].strip()),
    ('작은 TMI', st.session_state['fun_fact'].strip()),
    ('이상적인 주말', st.session_state['weekend'].strip()),
])
facts = [(label, detail) for label, detail in facts if detail]

fact_columns = st.columns(3, gap='large')
for index, (label, detail) in enumerate(facts):
    with fact_columns[index % len(fact_columns)]:
        st.markdown(
            f'<div class="fact"><div class="fact-label">{html.escape(label)}</div>'
            f'<div class="fact-value">{html.escape(detail)}</div></div>',
            unsafe_allow_html=True,
        )

if st.session_state['quote'].strip():
    st.markdown(f'> “{html.escape(st.session_state["quote"].strip())}”')

st.divider()
with st.expander('소개 정보 수정'):
    with st.form('profile_form'):
        name_col, gender_col = st.columns(2)
        with name_col:
            st.text_input('이름', key='name')
        with gender_col:
            st.text_input('성별', key='gender')

        nickname_col, location_col = st.columns(2)
        with nickname_col:
            st.text_input('별명', key='nickname')
        with location_col:
            st.text_input('거주지역', key='location')

        st.text_area('짧은 자기소개', key='intro', height=90)
        color_col, hobby_col = st.columns(2)
        with color_col:
            st.selectbox('좋아하는 컬러', list(COLOR_OPTIONS), key='favorite_color')
        with hobby_col:
            st.text_input('취미', key='hobby')

        food_col, animal_col = st.columns(2)
        with food_col:
            st.text_input('좋아하는 음식', key='food')
        with animal_col:
            st.text_input('가장 좋아하는 동물', key='animal')

        music_col, weekend_col = st.columns(2)
        with music_col:
            st.text_input('요즘 즐겨 듣는 음악', key='music')
        with weekend_col:
            st.text_input('이상적인 주말', key='weekend')

        st.text_input('작은 TMI', key='fun_fact')
        st.text_input('마음에 두는 문장', key='quote')
        st.text_input('인스타그램 · 링크', key='link')
        st.form_submit_button('소개 업데이트', type='primary', use_container_width=True)

download_lines = [f'# {name}']
if nickname:
    download_lines.append(f'별명: {nickname}')
if intro:
    download_lines.extend(['', intro])
download_lines.extend(['', '## 취향과 일상'])
download_lines.extend(f'- **{label}:** {detail}' for label, detail in facts)
if st.session_state['quote'].strip():
    download_lines.extend(['', f'> {st.session_state["quote"].strip()}'])
if st.session_state['link'].strip():
    download_lines.extend(['', f'링크: {st.session_state["link"].strip()}'])
st.download_button(
    '소개글 다운로드 (.md)',
    data='\n'.join(download_lines),
    file_name='seo-jihyeong-introduction.md',
    mime='text/markdown',
)