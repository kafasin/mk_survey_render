import streamlit as st

st.title("MEMOCAN ANKET")

# "sinan", st.session_state

if 'num' not in st.session_state:
    st.session_state.num = 0
    st.session_state['ind'] = 0


cevap1 = ['A', 'B', 'C', 'D']
cevap2 = ['E', 'F', 'G', 'H']

qs1 = [('Soru BIR', cevap1), ('Soru UC', cevap1), ('soru BES', cevap1)]
qs2 = [('Soru IKI', cevap2), ('Soru DORT', cevap2), ('Soru ALTI', cevap2)]


def main():
    for _, _ in zip(qs1, qs2):
        placeholder = st.empty()
        num = st.session_state.num
        ind = st.session_state['ind']
        with placeholder.form(key=str(num)):
            st.radio(qs1[ind][0], key=num+1, options=qs1[ind][1])
            st.radio(qs2[ind][0], key=num+2, options=qs2[ind][1])
            # st.write(st.session_state.num)
            if ind > 1:
                st.write("BITTI")
            else:
                st.write("SONRAKI SORU")

            if st.form_submit_button():
                st.session_state.num += 3
                st.session_state['ind'] += 1
                if st.session_state.num >= 9:
                    st.session_state.num = 0
                    st.session_state['ind'] = 0
                placeholder.empty()
            else:
                st.stop()


main()