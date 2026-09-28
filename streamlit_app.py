import html

import streamlit as st


st.set_page_config(
    page_title='나를 소개해요',
    page_icon='👋',
    layout='wide',
)

st.markdown(
    '''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #20312f;
        --muted: #687774;
        --green: #3f806b;
        --line: #e4ebe6;
        --paper: #ffffff;
        --canvas: #f4f7f3;
    }
    .stApp {
        background:
            radial-gradient(ellipse at 8% 4%, rgba(222, 239, 226, .72), transparent 30rem),
            var(--canvas);
        color: var(--ink);
        font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stMainBlockContainer"] { max-width: 1180px; padding-top: 2.5rem; }
    h1, h2, h3, p, label, button, input, textarea, [data-testid="stMarkdownContainer"] {
        font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    }
    .eyebrow {
        color: var(--green); font-size: .78rem; font-weight: 700;
        letter-spacing: .08em; text-transform: uppercase; margin-bottom: .45rem;
    }
    .page-title { color: var(--ink); font-size: 2.35rem; font-weight: 800; line-height: 1.2; margin: 0; }
    .page-subtitle { color: var(--muted); font-size: 1rem; margin: .65rem 0 1.6rem; }
    .section-title { color: var(--ink); font-size: 1.06rem; font-weight: 700; margin: .35rem 0 .25rem; }
    .section-note { color: var(--muted); font-size: .86rem; margin: 0 0 .8rem; }
    .profile-card {
        background: var(--paper); border: 1px solid var(--line); border-radius: 12px;
        padding: 1.5rem; box-shadow: 0 12px 36px rgba(35, 58, 47, .06);
    }
    .profile-top { display: flex; align-items: center; gap: 1rem; padding-bottom: 1.1rem; border-bottom: 1px solid var(--line); }
    .profile-dot { width: 54px; height: 54px; border-radius: 50%; flex: 0 0 54px; display: grid; place-items: center; font-size: 1.55rem; }
    .profile-name { color: var(--ink); font-size: 1.48rem; font-weight: 800; line-height: 1.3; }
    .profile-meta { color: var(--muted); font-size: .88rem; margin-top: .18rem; }
    .profile-intro { color: #3a4d48; font-size: .96rem; line-height: 1.75; white-space: pre-wrap; margin: 1rem 0; }
    .profile-tags { display: flex; flex-wrap: wrap; gap: .45rem; margin: .9rem 0 1.1rem; }
    .profile-tag { background: #f0f5f1; border-radius: 5px; color: #3d6556; font-size: .8rem; padding: .35rem .6rem; }
    .profile-grid { border-top: 1px solid var(--line); display: grid; grid-template-columns: 1fr 1fr; gap: .95rem 1rem; padding-top: 1rem; }
    .profile-label { color: var(--muted); font-size: .75rem; margin-bottom: .2rem; }
    .profile-value { color: var(--ink); font-size: .9rem; font-weight: 600; overflow-wrap: anywhere; white-space: pre-wrap; }
    .profile-quote { background: #f7f7ed; border-left: 3px solid #d3c66e; border-radius: 0 5px 5px 0; color: #5c593e; line-height: 1.6; margin-top: 1rem; padding: .75rem .85rem; }
    .preview-empty { background: rgba(255,255,255,.75); border: 1px dashed #cbd8ce; border-radius: 12px; color: var(--muted); line-height: 1.7; padding: 2rem 1.4rem; text-align: center; }
    div[data-testid="stForm"] { background: var(--paper); border: 1px solid var(--line); border-radius: 10px; padding: 1rem 1.15rem .35rem; }
    div[data-testid="stForm"] label { color: #455852; }
    .stButton button, .stDownloadButton button { border-radius: 6px; font-weight: 600; }
    @media (max-width: 640px) {
        [data-testid="stMainBlockContainer"] { padding: 1.2rem 1rem 2rem; }
        .page-title { font-size: 1.9rem; }
        .profile-grid { grid-template-columns: 1fr 1fr; }
    }
    </style>
    ''',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="eyebrow">A LITTLE ABOUT ME</div>'
    '<h1 class="page-title">나를 소개해요</h1>'
    '<p class="page-subtitle">나다운 정보들을 채우고, 한 장의 소개 카드로 정리해 보세요.</p>',
    unsafe_allow_html=True,
)

left, right = st.columns([1.08, 0.92], gap='large')

with left:
    st.markdown('<div class="section-title">소개 정보</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-note">편한 항목만 골라 적어도 좋아요.</div>', unsafe_allow_html=True)

    with st.form('profile_form'):
        st.markdown('**기본 정보**')
        name_col, nickname_col = st.columns(2)
        with name_col:
            st.text_input('이름', placeholder='예: 김하늘', key='name')
        with nickname_col:
            st.text_input('별명', placeholder='예: 하늘이', key='nickname')

        role_col, location_col = st.columns(2)
        with role_col:
            st.text_input('하는 일 · 관심 분야', placeholder='예: 디자이너, 식물', key='role')
        with location_col:
            st.text_input('사는 곳', placeholder='예: 서울', key='location')

        st.text_area('한 줄 또는 짧은 자기소개', placeholder='요즘 어떤 사람인지 자유롭게 적어 보세요.', key='intro', height=90)

        st.markdown('**취향과 일상**')
        color_col, hobby_col = st.columns(2)
        with color_col:
            color_options = {
                '초록': ('🌿', '#dceee3'),
                '파랑': ('🌊', '#dcebf4'),
                '노랑': ('☀️', '#f5edc9'),
                '분홍': ('🌸', '#f5e1e8'),
                '보라': ('🔮', '#eae3f3'),
                '주황': ('🍊', '#f5e5d5'),
            }
            favorite_color = st.selectbox('좋아하는 컬러', list(color_options), key='favorite_color')
        with hobby_col:
            st.text_input('취미', placeholder='예: 산책, 베이킹', key='hobby')

        food_col, music_col = st.columns(2)
        with food_col:
            st.text_input('좋아하는 음식', placeholder='예: 떡볶이', key='food')
        with music_col:
            st.text_input('요즘 즐겨 듣는 음악', placeholder='예: 재즈, 인디 팝', key='music')

        st.markdown('**나를 더 잘 보여주는 것들**')
        fun_col, weekend_col = st.columns(2)
        with fun_col:
            st.text_input('작은 TMI', placeholder='예: 커피보다 차를 좋아해요', key='fun_fact')
        with weekend_col:
            st.text_input('이상적인 주말', placeholder='예: 늦잠 자고 동네 산책', key='weekend')

        st.text_input('요즘 마음에 두는 문장', placeholder='예: 천천히 가도 괜찮아', key='quote')
        st.text_input('인스타그램 · 링크', placeholder='선택 사항', key='link')
        submitted = st.form_submit_button('소개 카드 만들기', type='primary', use_container_width=True)

with right:
    st.markdown('<div class="section-title">미리보기</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-note">완성된 소개 카드예요.</div>', unsafe_allow_html=True)

    if submitted:
        st.session_state['profile_ready'] = True

    if st.session_state.get('profile_ready'):
        value = lambda key: st.session_state.get(key, '').strip()
        name = value('name') or '이름을 입력해 주세요'
        nickname = value('nickname')
        role = value('role')
        location = value('location')
        intro = value('intro')
        favorite_color = st.session_state.get('favorite_color', '초록')
        color_emoji, color_hex = {
            '초록': ('🌿', '#dceee3'),
            '파랑': ('🌊', '#dcebf4'),
            '노랑': ('☀️', '#f5edc9'),
            '분홍': ('🌸', '#f5e1e8'),
            '보라': ('🔮', '#eae3f3'),
            '주황': ('🍊', '#f5e5d5'),
        }[favorite_color]
        meta = ' · '.join(part for part in [nickname and f'별명 {nickname}', role, location] if part)

        detail_items = [
            ('좋아하는 컬러', f'{color_emoji} {favorite_color}'),
            ('취미', value('hobby')),
            ('좋아하는 음식', value('food')),
            ('요즘 듣는 음악', value('music')),
            ('작은 TMI', value('fun_fact')),
            ('이상적인 주말', value('weekend')),
        ]
        details_html = ''.join(
            f'<div><div class="profile-label">{html.escape(label)}</div>'
            f'<div class="profile-value">{html.escape(detail)}</div></div>'
            for label, detail in detail_items if detail
        )
        tags_html = ''.join(
            f'<span class="profile-tag">{html.escape(tag)}</span>'
            for tag in [role, location] if tag
        )
        quote_html = (
            f'<div class="profile-quote">“{html.escape(value("quote"))}”</div>'
            if value('quote') else ''
        )
        intro_html = f'<div class="profile-intro">{html.escape(intro)}</div>' if intro else ''
        tags_section = f'<div class="profile-tags">{tags_html}</div>' if tags_html else ''
        link_html = (
            f'<div class="profile-label">링크</div><div class="profile-value">{html.escape(value("link"))}</div>'
            if value('link') else ''
        )

        st.markdown(
            f'<div class="profile-card">'
            f'<div class="profile-top"><div class="profile-dot" style="background:{color_hex}">{color_emoji}</div>'
            f'<div><div class="profile-name">{html.escape(name)}</div>'
            f'<div class="profile-meta">{html.escape(meta or "반가워요!")}</div></div></div>'
            f'{intro_html}{tags_section}'
            f'<div class="profile-grid">{details_html}{link_html}</div>{quote_html}</div>',
            unsafe_allow_html=True,
        )

        markdown_lines = [f'# {name}']
        if meta:
            markdown_lines.append(f'_{meta}_')
        if intro:
            markdown_lines.extend(['', intro])
        markdown_lines.extend(['', '## 취향과 일상'])
        markdown_lines.extend(f'- **{label}:** {detail}' for label, detail in detail_items if detail)
        if value('quote'):
            markdown_lines.extend(['', f'> {value("quote")}'])
        if value('link'):
            markdown_lines.extend(['', f'링크: {value("link")}'])
        st.download_button(
            '소개글 다운로드 (.md)',
            data='\n'.join(markdown_lines),
            file_name='my-introduction.md',
            mime='text/markdown',
            use_container_width=True,
        )
    else:
        st.markdown(
            '<div class="preview-empty">'
            '<div style="font-size:2rem; margin-bottom:.5rem">✍️</div>'
            '왼쪽에 소개 정보를 적고<br><b>소개 카드 만들기</b>를 눌러 주세요.'
            '</div>',
            unsafe_allow_html=True,
        )