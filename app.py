import streamlit as st

# Set page config first
st.set_page_config(page_title="Medical Information and Consent")

# Include the Google Fonts link and style within st.markdown() call
st.markdown("""
    <head>
        <link href="https://fonts.googleapis.com/css?family=Kanit&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Kanit', Tahoma, sans-serif;
                margin: 20px;
                line-height: 1.6;
            }
            .section {
                margin-bottom: 20px;
            }
            .consent-button {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 4px;
            }
        </style>
    </head>
    """, unsafe_allow_html=True)

# Set up a session state variable for language and consent
if 'language' not in st.session_state:
    st.session_state['language'] = 'en'

if 'consent_accepted' not in st.session_state:
    st.session_state['consent_accepted'] = False

# Language switcher function
def switch_language(language):
    st.session_state['language'] = language

# Function to toggle consent acceptance
def toggle_consent():
    st.session_state['consent_accepted'] = not st.session_state['consent_accepted']

# Language Switch Buttons
st.sidebar.title("Language")
st.sidebar.button("English", on_click=switch_language, args=('en',))
st.sidebar.button("ภาษาไทย", on_click=switch_language, args=('th',))

# English Content
if st.session_state['language'] == 'en':
    st.markdown("""
    <div class="section">
        <h2>Medical Information Details</h2>
        <p>This application is designed to analyze users' cough sounds to assess the risk of pneumonia, bronchitis, and COVID-19.</p>
        <p><strong>Limitations of Information:</strong></p>
        <ul>
            <li>This analysis cannot replace the examination and diagnosis by a healthcare professional.</li>
            <li>The results provided are only preliminary predictions and may not always be accurate.</li>
            <li>Users should consult a doctor or medical expert for an accurate diagnosis.</li>
        </ul>
        <p><strong>Additional Information:</strong></p>
        <ul>
            <li>The recorded sounds will not be saved or stored in our system.</li>
            <li>This application does not collect any personally identifiable information, such as name, address, or other personal data.</li>
            <li>The data used for analysis will be automatically deleted after the analysis is complete.</li>
        </ul>
        <p><strong>Privacy Rights:</strong></p>
        <ul>
            <li>This application respects and complies with data protection principles as required by applicable law.</li>
            <li>All data used for analysis will be kept confidential and will not be disclosed to third parties without the user's consent.</li>
        </ul>
        <h2>Consent Agreement</h2>
        <p>By using this application, you agree to the following terms:</p>
        <ul>
            <li><strong>Voluntary Participation:</strong> Your use of this application is voluntary. There is no coercion involved.</li>
            <li><strong>Data Usage:</strong> The application will use your cough sound for analysis without saving or storing any data. All data will be automatically deleted after the analysis is complete.</li>
            <li><strong>Accuracy of Information:</strong> The information derived from the analysis is only a preliminary prediction and cannot replace a diagnosis by a healthcare professional.</li>
            <li><strong>Data Protection:</strong> Your information will not be used for identification or shared with third parties without your consent.</li>
        </ul>
        <input type="checkbox" id="consentCheckbox" onchange="toggleConsent(this)">
        <label for="consentCheckbox">I accept and understand the above terms</label>
    </div>
    """, unsafe_allow_html=True)

# Thai Content
elif st.session_state['language'] == 'th':
    st.markdown("""
    <div class="section">
        <h2>รายละเอียดข้อมูลทางการแพทย์</h2>
        <p>แอปพลิเคชั่นนี้ถูกออกแบบมาเพื่อวิเคราะห์เสียงไอของผู้ใช้เพื่อตรวจสอบความเสี่ยงในการเป็นโรคปอดอักเสบ, โรคหลอดลมอักเสบ, และ COVID-19</p>
        <p><strong>ข้อจำกัดของข้อมูล:</strong></p>
        <ul>
            <li>การวิเคราะห์นี้ไม่สามารถทดแทนการตรวจสอบและวินิจฉัยโดยแพทย์ผู้เชี่ยวชาญได้</li>
            <li>ข้อมูลที่แสดงผลเป็นเพียงการคาดการณ์เบื้องต้นเท่านั้น และอาจไม่ถูกต้องเสมอไป</li>
            <li>ผู้ใช้ควรปรึกษาแพทย์หรือผู้เชี่ยวชาญด้านการแพทย์เพื่อรับการวินิจฉัยที่แม่นยำ</li>
        </ul>
        <p><strong>ข้อมูลเพิ่มเติม:</strong></p>
        <ul>
            <li>การอัดเสียงจะไม่ถูกบันทึกหรือเก็บข้อมูลใดๆ ในระบบของเรา</li>
            <li>แอปพลิเคชั่นนี้ไม่มีการเก็บข้อมูลที่สามารถใช้ในการระบุตัวตนผู้ใช้ เช่น ชื่อ, ที่อยู่, หรือข้อมูลส่วนบุคคลอื่นๆ</li>
            <li>ข้อมูลที่ถูกใช้ในการวิเคราะห์จะถูกลบอัตโนมัติหลังจากการวิเคราะห์เสร็จสิ้น</li>
        </ul>
        <p><strong>สิทธิ์ส่วนบุคคล:</strong></p>
        <ul>
            <li>แอปพลิเคชั่นนี้เคารพและปฏิบัติตามหลักการคุ้มครองข้อมูลส่วนบุคคลตามกฎหมายที่บังคับใช้</li>
            <li>ข้อมูลทั้งหมดที่ใช้ในการวิเคราะห์จะถูกเก็บรักษาเป็นความลับและไม่ถูกเปิดเผยต่อบุคคลภายนอกโดยไม่ได้รับความยินยอมจากผู้ใช้</li>
        </ul>
        <h2>ข้อตกลงการยินยอม</h2>
        <p>โดยการใช้แอปพลิเคชั่นนี้ คุณยินยอมและเข้าใจข้อกำหนดดังต่อไปนี้:</p>
        <ul>
            <li><strong>ความสมัครใจ:</strong> การใช้แอปพลิเคชั่นนี้เป็นไปตามความสมัครใจของคุณ ไม่มีการบังคับใดๆ</li>
            <li><strong>การใช้ข้อมูล:</strong> แอปพลิเคชั่นจะใช้เสียงไอของคุณเพื่อวิเคราะห์โรคโดยไม่บันทึกหรือเก็บข้อมูลใดๆ ข้อมูลทั้งหมดจะถูกลบอัตโนมัติหลังจากการวิเคราะห์เสร็จสิ้น</li>
            <li><strong>ความถูกต้องของข้อมูล:</strong> ข้อมูลที่ได้จากการวิเคราะห์เป็นเพียงการคาดการณ์เบื้องต้นเท่านั้น และไม่สามารถทดแทนการวินิจฉัยโดยแพทย์ผู้เชี่ยวชาญได้</li>
            <li><strong>การคุ้มครองข้อมูลส่วนบุคคล:</strong> ข้อมูลของคุณจะไม่ถูกใช้เพื่อการระบุตัวตนหรือแบ่งปันกับบุคคลภายนอกโดยไม่ได้รับความยินยอมจากคุณ</li>
        </ul>
        <input type="checkbox" id="consentCheckbox" onchange="toggleConsent(this)">
        <label for="consentCheckbox">ข้าพเจ้ายอมรับและเข้าใจข้อตกลงข้างต้น</label>
    </div>
    """, unsafe_allow_html=True)

# JavaScript to toggle consent acceptance
consent_script = """
<script>
    function toggleConsent(checkbox) {
        var consentButton = document.getElementById('consentButton');
        consentButton.disabled = !checkbox.checked;
    }
</script>
"""

# Display JavaScript
st.markdown(consent_script, unsafe_allow_html=True)

# Next button to go to the next page
if st.session_state['consent_accepted']:
    st.button('Next', key='consentButton', on_click=lambda: st.experimental_rerun())
