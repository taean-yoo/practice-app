import streamlit as st
import datetime

st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="./images/monsterball.png"
)


st.title("맛집 리스트")
st.markdown("**울산 맛집**을 추가해서 리스트를 채워보세요!")

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "언제 갔나요?",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)
d
type_emoji_dict = {
    "한식": "⚪",
    "중식": "✊",
    "양식": "🕊",
    "일식": "☠️",
    "기타": "🌋",
}

initial_restaruant= [
    {
        "name": "유니스트 학식",
        "types": ["한식"],
        "image_url": "https://i.namu.wiki/i/TCYHnImJHz7afWZWpS--GI0ecalq3wILFd-io09I1rs0vquk5CD38XvqwAvGyId1EsNwqTKvdg9bO1Zxap_984ROSyBkWk_pPcUwLNDDItzzGhK9VRT7zWZQCOfCdlpdNCV1qYvyDug_j58go9_Deg.webp"
    },
]

if "restaurant" not in st.session_state:
    st.session_state.restaurant = initial_restaruant


example = {
    "name": "교직원 식당",
    "types": ["한식"],
    "date": "2024-10-04"
}

auto_complete = st.toggle("예시 데이터로 채우기")
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="맛집 이름",
            value=example["name"] if auto_complete else ""
        )
    with col2:
        types = st.multiselect(
            label="유형",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example["types"] if auto_complete else []
        )
    date = st.text_input(
        label="날짜",
        value=example["date"] if auto_complete else ""
    )
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("맛집 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("유형을 적어도 한개 선택해주세요")
        else:
            st.success("맛집을 추가할 수 있습니다.")
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                "date": date if date else "https://i.namu.wiki/i/TCYHnImJHz7afWZWpS--GI0ecalq3wILFd-io09I1rs0vquk5CD38XvqwAvGyId1EsNwqTKvdg9bO1Zxap_984ROSyBkWk_pPcUwLNDDItzzGhK9VRT7zWZQCOfCdlpdNCV1qYvyDug_j58go9_Deg.webp"
            })

for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon['name']}**", expanded=True):
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text(" / ".join(emoji_types))
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    del st.session_state.pokemons[i+j]
                    st.rerun()