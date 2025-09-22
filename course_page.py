import streamlit as st
import os
import base64
import streamlit_pdf
from courses.excel import assessments

images_dir = os.path.join(os.path.dirname(__file__), "media")
medias = [
    os.path.join(images_dir, "excel_medias.png"),
    os.path.join(images_dir, "scholarracourselogo.png"),
    os.path.join(images_dir, "courseimage.jpg"),
    os.path.join(images_dir, "Syllabus TTS.mp3"),
    os.path.join(images_dir, "mo-200-microsoft-excel-2019-skills-measured (2).pdf"),
    os.path.join(images_dir, "Excel-Fundamentals-Manual.pdf"),
    os.path.join(images_dir, "cat.png")
    
]

import streamlit as st

def take_quiz(quiz_dict, lesson_name="Lesson 1"):
    st.header(f"{lesson_name} Quiz")
    user_answers = {}
    
    # Display each question and get answer
    for i, (question, correct_answer) in enumerate(quiz_dict.items()):
        user_input = st.text_input(question, key=f"{lesson_name}_{i}")
        user_answers[question] = user_input
    
    if st.button("Submit"):
        score = 0
        for question, correct_answer in quiz_dict.items():
            if user_answers.get(question, "").strip().lower() == correct_answer.strip().lower():
                score += 1
        
        total_questions = len(quiz_dict)
        percentage = (score / total_questions) * 100
        st.success(f"You got {score} out of {total_questions} correct! ({percentage:.1f}%)")

# Example usage:
# take_quiz(lesson_3_quiz, "Lesson 3")


def url_video_func(url, name, video_title):
    contain((video_title, 25, 0))
    st.write("")
    st.video(url)
    video_credit_expander = st.container() 
    
    with video_credit_expander:
        st.markdown(
            f'''
            <details style="
                background-color: #FFFFFF;
                color: black;
                border: 2px solid #e6e6e6;
                border-radius: 10px;
                padding: 12px 20px;
                font-size: 16px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            ">
                <summary style="font-weight:bold; font-size:18px; cursor:pointer;">
                    Video credit
                </summary>
                <div style="margin-top:10px;">
                    Video produced by <strong>{name}</strong> on Youtube.<br>
                    URL: <a href="{url}" target="_blank">{url}</a>
                </div>
            </details>
            ''',
            unsafe_allow_html=True
        )



def navigation_buttons(id1,id2):
    if "prog" not in st.session_state:
        st.session_state.prog = 1
    # CSS styling for buttons
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #FFFFFF;
            color: black;
            border: 2px solid #e6e6e6;
            border-radius: 5px;
            padding: 8px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    # Three columns: left button, spacer, right button
    col1, col2, col3 = st.columns([1, 8, 1])

    # Back button (left)
    with col1:
        if st.button("Back", key=id1):
            st.session_state.prog -= 1
            st.rerun()

    # Spacer column col2 does nothing (just stretches space)

    # Next button (right)
    with col3:
        if st.button("Next", key=id2):
            st.session_state.prog += 1
            st.rerun()

    # Display current value centered
    st.progress((st.session_state.prog / 9), width="stretch")

def contain(*messages):
    # Start the div with styles
    html_content = '<div style="border:2px solid #e6e6e6; background-color:#FFFFFF; padding:10px; border-radius:10px;">'
    
    # Add each message to the div
    for msg, size, align in messages:
        alignment = ["center", "left", "right"]
        html_content += f'<p style="text-align:{alignment[align]}; font-size:{size}px;">{msg}</p>'
    
    # Close the div
    html_content += '</div>'
    
    # Render everything at once
    st.markdown(html_content, unsafe_allow_html=True)

def display_course():
    if "prog" not in st.session_state:
        st.session_state.prog = 1
    if st.session_state.page == 2:
        
        with open(medias[2], "rb") as image_file:
            bg_encoded = base64.b64encode(image_file.read()).decode()
        
        with open(medias[1], "rb") as image_file:
            fg_encoded = base64.b64encode(image_file.read()).decode()
        
        st.markdown(
            f"""
            <style>
            /* Background banner */
            .course-banner-wrapper {{
                position: relative;
                width: 100%;
                height: 600px;
                background-image: url("data:image/png;base64,{bg_encoded}");
                background-size: cover;
                background-position: center bottom;
                background-repeat: no-repeat;
                overflow: hidden;
            }}

            /* Foreground content */
            .course-banner-foreground {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 400px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                z-index: 2;
            }}

            /* Foreground medias */
            .course-banner-foreground img {{
                width: 600px;
                height: auto;
                margin-bottom: 10px;
            }}

            /* Foreground text */
            .course-banner-foreground p {{
                font-size: 25px;
                font-weight: 700;
                color: white;
                text-shadow: 2px 2px 5px rgba(0,0,0,0.6);
                margin: 0;
            }}
            </style>

            <div class="course-banner-wrapper" id="courseBanner">
                <div class="course-banner-foreground">
                    <img src="data:image/png;base64,{fg_encoded}">
                    <p>Smarter study starts here.</p>
                </div>
            </div>

            <script>
            window.addEventListener('scroll', function() {{
                var banner = document.getElementById('courseBanner');
                var scrollTop = window.pageYOffset;
                var yPos = -(scrollTop * 0.3); // adjust speed here
                banner.style.backgroundPosition = 'center ' + yPos + 'px';
            }});
            </script>
            """,
            unsafe_allow_html=True
        )
    
    tab1, tab2 = st.tabs(["Excel", "Intro to ML"])
    
    with tab1:
        if st.session_state.prog <= 1:
            contain(
                ("MO-200 Excel", 40, 0),
                ("Welcome! We're so glad you've chosen to enroll in our excel prep program! Feel free to look through the course syllabus. Once done scroll down and click next.", 25, 0)
            )
            st.audio(medias[3])
            contain(
                ("Course Syllabus", 25, 0)
            )
            st.write("")
            st.pdf(medias[4])
            contain(
                ("Excel Manual", 25, 0)
            )
            st.write("")
            st.pdf(medias[5])
            navigation_buttons(1,2)
        elif st.session_state.prog == 2:
            url_video_func("https://www.youtube.com/watch?v=EaS2Ooe9BNc&t=67s", "Kevin Stratvert", "How to import PDF into Excel" )
            url_video_func("https://www.youtube.com/watch?v=ebnNy5yEkvc", "ProgrammingKnowledge2", "How to Import CSV File Into Excel")
            navigation_buttons(3,4)
        elif st.session_state.prog == 3:
            contain(
                ("Lesson 2, navigating workbook", 40, 0),
                ("""In this lesson, we will explore how to efficiently move through and manage the contents of a workbook. 
                    You’ll learn how to search for specific data, jump directly to named cells or ranges, and access different workbook elements with ease. 
                    Additionally, we’ll cover how to insert and remove hyperlinks, making it easier to connect information within your workbook or to external resources. 
                    Mastering these skills will help you work faster, stay organized, and make your spreadsheets more interactive and user-friendly.""", 25, 0)
            )
            url_video_func("https://www.youtube.com/watch?v=ovDpZD4BxQk", "Kay Rand Morgan", "Search for data within a workbook" )
            url_video_func("https://www.youtube.com/watch?v=Z7RQnu3yrPk", "Kay Rand Morgan", "Navigating to named cells, ranges, or workbook elements" )
            url_video_func("https://www.youtube.com/watch?v=QMzx3h-USM4", "Santhu Analytics", "How to Create & Remove Hyperlinks" )
            take_quiz(assessments.lesson_2_quiz, "Lesson 2")
            navigation_buttons(5,6)
        elif st.session_state.prog == 4:
            contain(("Lesson 3, formatting", 40, 0),
                    ("In this lesson, you’ll learn how to format worksheets and workbooks, modify page setup for printing and presentation, adjust row height and column width, and customize headers and footers. These skills will help you organize data more effectively, improve the readability of your spreadsheets, and ensure your work is presented in a clear and professional manner.", 25, 0)
            )
            url_video_func("https://www.youtube.com/watch?v=0SRt9dkR3Zg", "learnexcel.video","Excel Page Layout: The Ultimate Guide")
            url_video_func("https://www.youtube.com/watch?v=wI6U9I2nZWg", "Technology for Teachers and Students", "3 Ways to AutoFit all Columns and Rows in Excel")
            url_video_func("https://www.youtube.com/watch?v=UbYcYXfHwII", "Technology for Teachers and Students", "Create Custom Headers and Footers in Excel")
            take_quiz(assessments.lesson_3_quiz, "Lesson 3")
            navigation_buttons(5,6)
        elif st.session_state.prog == 5:
            contain(("Lesson 3.1, customization", 40, 0),
                    ("In this lesson, you’ll learn how to customize the Quick Access Toolbar, display and modify workbook content in different views, freeze worksheet rows and columns, change window views, modify basic workbook properties, and display formulas. Mastering these features will make navigating Excel more efficient, allow you to organize and review data with greater ease, and give you more control over how your workbook is displayed and managed.", 25, 0)
            )
            url_video_func("https://www.youtube.com/watch?v=ERCg7RznD3w", "Simon Sez IT", "Customize the Quick Access toolbar")
            url_video_func("https://www.youtube.com/watch?v=rqjStG5xTZ4", "Kay Rand Morgan", "Display and modify workbook content in different views")
            url_video_func("https://www.youtube.com/watch?v=UJ4vPQ18PLg", "Excel Rush", "How to Freeze Multiple Rows and or Columns in Excel using Freeze Panes")
            url_video_func("https://www.youtube.com/watch?v=GfHWyniYja4", "Kay Rand Morgan", "Change window views")
            url_video_func("https://www.youtube.com/watch?v=5ta5Vf8VRms", "David Hays", "Modify basic workbook properties")
            url_video_func("https://www.youtube.com/watch?v=nBkv7EGsAIU", "Excel Tutorials by EasyClick Academy", "Display formulas")
            take_quiz(assessments.lesson_3_1_quiz, "Lesson 3.1")
            navigation_buttons(5,6)
        elif st.session_state.prog == 6:
            contain(("Lesson 4, how to configure for collaboration", 40, 0),
                    ("In this lesson, you’ll learn how to set a print area, save workbooks in alternative file formats, configure print settings, and inspect workbooks for issues. These skills will ensure your spreadsheets are prepared for sharing, printing, and distribution while maintaining accuracy, compatibility, and professionalism.", 25, 0)
            )
            url_video_func("https://www.youtube.com/watch?v=Mrt4v0ysA8w", "Excel Tutorials by EasyClick Academy", "How to Set the Print Area in Excel (Step by Step)")
            url_video_func("https://www.youtube.com/watch?v=P2L4GOGDsx8", "Kay Rand Morgan", "Microsoft Excel - Save workbooks in alternative file formats CC")
            url_video_func("https://www.youtube.com/watch?v=HfwMo6M1XzM", "Kevin Stratvert", "How to Print Excel Sheet")
            url_video_func("https://www.youtube.com/watch?v=KbJUKAY8FZ8", "How To Tutorials- Maha Gurus", "Inspecting and Protecting Workbooks- Inspect Document in Excel Tutorial")
            take_quiz(assessments.lesson_4_quiz, "Lesson 4")
            navigation_buttons(7,8)
        elif st.session_state.prog == 7:
            contain(("Lesson 5, formatting cells and ranges", 40, 0),
                    ("In this lesson, you’ll learn how to merge and unmerge cells, modify cell alignment, orientation, and indentation, format cells using the Format Painter, and wrap text within cells. You’ll also explore how to apply number formats, use the Format Cells dialog box, apply cell styles, and clear cell formatting. Together, these skills will help you present data clearly, maintain consistency in your worksheets, and create professional, easy-to-read spreadsheets.", 25, 0)
            )
            url_video_func("https://www.youtube.com/watch?v=b0T9XjhBK_g", "Microsoft 365", "How to merge and unmerge cells in Microsoft Excel")
            url_video_func("https://www.youtube.com/watch?v=FljG3k2Ly6s", "Kay Rand Morgan", "Microsoft Excel - Modify cell alignment, orientation, and indentation CC")
            url_video_func("https://www.youtube.com/watch?v=LHSJJvkVrvA", "LearnFree", "Excel Quick Tip: Two Ways to Use the Format Painter")
            url_video_func("https://www.youtube.com/watch?v=fu0o9fkkMWI", "Technology for Teachers and Students", "3 Ways to Fit Excel Data within a Cell")
            url_video_func("https://www.youtube.com/watch?v=fjyOG7Ls7BA", "LearnFree", "Excel: Understanding Number Formats")
            url_video_func("https://www.youtube.com/watch?v=FwI46frGd9k", "KnowWithBeau", "Excel MOS 2.2.6 Apply cell formats from the Format Cells dialog box - KwB")
            url_video_func("https://www.youtube.com/watch?v=YSsQmEPFNaI", "Simon Sez IT", "Using Cell Styles in Excel")
            url_video_func("https://www.youtube.com/watch?v=B9ol_9_QmJU", "ExcelHow Tech", "How to Clear Cell Contents and Formatting")
            take_quiz(assessments.lesson_5_quiz, "Lesson 5")
            navigation_buttons(9,10)
        elif st.session_state.prog == 8:
            contain(("Lesson 6, manipulating data in worksheets", 40, 0),
                    ("In this lesson, you’ll learn how to paste data by using special paste options, fill cells efficiently with Auto Fill, and insert or delete multiple columns, rows, or individual cells. These skills will help you manage and organize data more effectively, saving time while ensuring your worksheets remain accurate and well-structured.", 40, 0)
            )
            url_video_func("https://www.youtube.com/watch?v=_ODK4XW-aNs", "HowcastTechGadgets", "How to Use Paste Special | Microsoft Excel")
            url_video_func("https://www.youtube.com/watch?v=HMXLU9TGogc", "Excel Tutorials by EasyClick Academy", "How to Use AutoFill in Excel (Best Practices)")
            url_video_func("https://www.youtube.com/watch?v=JvSoAAkcWyY", "Microsoft 365", "How to insert or delete rows and columns in Microsoft Excel")
            take_quiz(assessments.lesson_6_quiz, "Lesson 6")
            navigation_buttons(11,12)
        elif st.session_state.prog >= 9:
            contain(("Congratulations!", 40, 0),
                    ("You've completed the excel course!", 40, 0)
                   )
            contain(("What next?", 40 ,0),
                   ("Let your teacher know! After that, follow their instructions and enroll for an official MO-200 ceritifcation exam!", 40, 0)
                   )
            contain(("Goodluck!", 40, 0),
                   )
            navigation_buttons(13,14)


    with tab2:
        contain(("Nothing to see here..", 40, 0),
                ("We're still working on this course. In the mean time, look after this guy.", 25, 0)
        )
        st.image(medias[6], width="stretch")



