# Определение персонажей игры.
define N = Character(None)
define H = Character ("Hastings", color = "#0e2838")
define P = Character ("Poirot", color = "#550c68")
define J = Character ("John Cavendish", color = "#324817")
define M = Character ("Mary Cavendish", color = "#893d5f")
define L = Character ("Lawrence Cavendish", color = "#2e4753")
define C = Character ("Cynthia", color = "#3c266f")
define E = Character ("Emily Inglethorp", color = "#803f28")
define A = Character ("Alfred Inglethorp", color = "#1c4b20")
define S = Character ("Dorcas", color = "#49491a")

# Фоны:
image bg exterior_day = "bg/exterior_day.jpg"
image bg hall = "bg/hall.jpg"
image bg garden = "bg/garden.jpg"
image bg library = "bg/library.jpg"
image bg guestroom = "bg/guestroom.jpg"
image bg hall2 = "bg/hall2.jpg"
image bg guestroom_ev = "bg/guestroom_ev.jpg"
image bg study = "bg/study.jpg"
image bg corridor = "bg/corridor.jpg"
image bg emily_room = "bg/emily_room.jpg"
image bg kitchen = "bg/kitchen.jpg"

# Персонажи:
image john = "char/john.png"
image mary = "char/mary.png"
image lawrence = "char/lawrence.png"
image cynthia = "char/cynthia.png"
image emily = "char/emily.png"
image alfred = "char/alfred.png"
image dorkas = "char/dorkas.png"
image poirot = "char/poirot.png"

# ---------------------------------------------------------
# ДАННЫЕ: записная книжка, улики, подозрения
# ---------------------------------------------------------
default notebook = []
default clues = {}
default suspicion = { "Alfred":0, "John":0, "Mary":0, "Lawrence":0, "Cynthia":0 }

init python:
    def add_note(text):
        if text not in notebook:
            notebook.append(text)
    def add_clue(key, text):
        if key not in clues:
            clues[key] = True
            add_note(text)

default notebook_page = 0
define NOTES_PER_PAGE = 5   # Сколько заметок показывать на одной странице
screen notebook_panel():
    tag notebook
    modal False
    frame:
        xalign 0.98
        yalign 0.02
        has vbox

        text "Notebook" size 26

        if notebook:
            $ start = notebook_page * NOTES_PER_PAGE
            $ end = start + NOTES_PER_PAGE
            $ notes_to_show = notebook[start:end]

            for n in notes_to_show:
                text "• [n]" size 20 xmaximum 360

            hbox:
                spacing 10
                if notebook_page > 0:
                    textbutton "← Back" action SetVariable("notebook_page", notebook_page - 1)
                if end < len(notebook):
                    textbutton "Next →" action SetVariable("notebook_page", notebook_page + 1)
        else:
            text "It's empty so far." size 20

    key "n" action Hide("notebook_panel")

screen ui_overlay():
    textbutton "Notebook [len(notebook)]":
        xalign 0.98
        yalign 0.02
        action ToggleScreen("notebook_panel")
    key "n" action ToggleScreen("notebook_panel")

init python:
    if "ui_overlay" not in config.overlay_screens:
        config.overlay_screens.append("ui_overlay")

# winding
# ivy
# gravel
# assistance
# estate
# acquaintances
# engage
# examine
# precision
# initial
# cautious
# excessively
# refrain
# maintain
# vibrant
# delight
# assist
# circumstances 
# acquired 
# surroundings
# hedge
# gathering
# assembly
# muffle
# proceed
# firm
# mahogany
# inspect
# brew
# Observe
# rapidly
# Resume
# obligations 
# Investigate 
# disturbance
# Fatigue
# overwhelmed
# curiosity
# Faint 
# flicker
# extinguish

# ---------------------------------------------------------
# ГЛАВА 1 — ПРИБЫТИЕ В СТАЙЛЗ
# ---------------------------------------------------------
label start:

    scene bg exterior_day with fade
    play music "audio/strings_manor_day.mp3" fadein 1.2

    N "On a bright afternoon, the winding road led me to Styles Court, a quiet mansion which didn't attract much attention. The facade looked welcoming — ivy embraced the walls, a gravel path led to the oak door, sunlight reflected on the windows."
    $ add_note ("Winding - a path/road, etc that bends a lot and is not straight.")
    $ add_note ("Ivy - a dark green plant that often grows up walls.")
    $ add_note ("Gravel - small pieces of stone used to make paths and road surfaces.")

    show john at right
    J "Hastings! Long time no see, we missed London's news."
    H "John, glad to see you again. Everything appears unchanged here... at first sight."

    scene bg hall with dissolve
    N "There was the scent of polished oak and fresh flowers in the hall. A servant took my luggage to the house."
    show dorkas at center
    S "Your belongings will be delivered to your room momentarily, sir." 
    H "Thank you, I appreciate your assistance."
    $ add_note("Assistance - help.")
    hide dorkas with dissolve
    
    menu:
        "Who should I approach for introductions and conversation?"
        "Greet the lady of the house":
            jump ch1_meet_emily
        "Discuss matters with John regarding family affairs":
            jump ch1_meet_john
        "Explore the surroundings (garden/library)":
            jump ch1_free_roam_intro

label ch1_meet_emily:

    show emily at center
    E "Welcome to our home. I hope the peaceful atmosphere and gardens will provide you with relaxation."
    H "Thank you for the warm welcome. The estate is truly magnificent."
    $ add_note("Estate - a large area of land in the countryside that is owned by one person or organization.")
    hide emily with dissolve
    menu:
        "Continue making acquaintances"
        "Introduce myself to Alfred":
            jump ch1_meet_alfred
        "Engage John and Mary in conversation":
            jump ch1_meet_mary
        "Request permission to examine the library":
            jump ch1_free_roam_intro
    $ add_note("Acquaintance - someone who you know but do not know well.")
    $ add_note("Engage - to interest someone in something and keep them thinking about it.")
    $ add_note("Examine - to look at someone or something very carefully, especially to try to discover something.")

label ch1_meet_alfred: 

    show alfred at right
    A "A pleasure to make your acquaintance. We value precision and routine here, and I hope you'll appreciate these qualities."
    $ add_note("Precision - the quality of being very exact and accurate.")
    H "Of course, I will respect both the customs and the rules of this house."
    $ suspicion["Alfred"] += 1
    menu:
        "What's your initial impression of Alfred?"
        "He's too reserved":
            H"(His politeness looks unnatural.)"
        "He is excessively cautious.":
            H "(He appears to measure every word with deliberate precision.)"
            $ suspicion["Alfred"] += 1
        "Refrain from premature conclusions.":
            pass
    $ add_note("Initial - first, or happening at the beginning.")
    $ add_note("Excessively - more than is necessary or wanted.")
    $ add_note("Cautious - taking care to avoid risks or danger.")
    $ add_note("Refrain - to stop yourself from doing something.")
    hide alfred with dissolve
    jump ch1_meet_mary

label ch1_meet_john:

    show john at right
    J "The family maintains appearances, though everyone has their own concerns. As expected, my mother remains active."
    $ add_note("Maintain - to make a situation or activity continue in the same way.")
    H "This shows that the household continues its vibrant activity."
    $ add_note("Vibrant - full of excitement and energy.")
    hide john with dissolve

    menu:
        "Who should I approach next?"
        "Mary Cavendish":
            jump ch1_meet_mary
        "Cynthia":
            jump ch1_meet_cynthia
        "Lawrence":
            jump ch1_meet_lawrence

label ch1_meet_mary:

    show mary at left
    M "Delighted to make your acquaintance. The garden is particularly splendid this time — if you prefer peaceful environment."
    H "I adore it. The garden is wonderful."
    $ add_note("Delight - happiness and excited pleasure.")
    
    menu:
        "Respond to Mary"
        "Suggest a walk in the garden":
            jump ch1_garden_first
        "Shift the conversation to the estate's architecture":
            H "The house seems to be very secure."
            M "The mansion has a rich history."
            jump ch1_branch_more_people
    hide mary with dissolve

label ch1_meet_cynthia:
    hide mary with dissolve
    show cynthia at left
    C "Good afternoon! I frequently assist at the village hospital's pharmacy — if you require any medicines, you can contact me."
    $ add_note("Assist - to help.")
    H "I hope circumstances don't require it, but the information is valuable anyway."
    $ add_note("Circumstances - facts or events that make a situation the way it is.")
    hide cynthia with dissolve
    jump ch1_branch_more_people

label ch1_meet_lawrence:

    hide mary with dissolve
    show lawrence at left
    L "You have chosen a good time — the library has recently acquired several rare editions."
    $ add_note("Acquired - to get something.")
    H "That sounds particularly intriguing."
    hide lawrence with dissolve
    jump ch1_branch_more_people

label ch1_branch_more_people:

    menu:
        "Who remains to be introduced?"
        "Meet Emily and Alfred":
            jump ch1_meet_emily
        "Approach Cynthia":
            jump ch1_meet_cynthia
        "Approach Lawrence":
            jump ch1_meet_lawrence
        "Conclude introductions":
            jump ch1_free_roam_intro

# Free overview of locations 
label ch1_free_roam_intro:

    N "I had leisure time before dinner. It was a perfect chance to explore surroundings."
    $ add_note("Surroundings - the place where someone or something is and the things that are in it.")
    jump ch1_hub

label ch1_hub:

    menu:
        "Which area requires exploration?"
        "Garden — pathways, hedges, summerhouse":
            jump ch1_garden_first
        "Library — documents, letters, books":
            jump ch1_library_first
        "Guest room — settle belongings":
            jump ch1_guestroom_first
        "Join the gathering — evening assembly in the hall":
            jump ch1_evening
    $ add_note("Hedge - a row of bushes growing close together, often used to divide land into separate areas.")
    $ add_note("Gathering - a party or a meeting when many people get together as a group.")
    $ add_note("Assembly - a regular meeting of all the students and teachers at a school.")

label ch1_garden_first:

    scene bg garden with dissolve
    N "The atmosphere in the garden was peaceful. Birds were singing and  leaves were rustling. Muffled voices could be heard from a distant arbor."
    $ add_note("Muffle - to make a noise quieter and less clear.")
    menu:
        "How should I proceed?"
        "Approach carefully to overhear":
            H " (The discussion was intense. The woman's voice remained firm, while the man was rather irritated.)"
            $ suspicion["Alfred"] += 1
        "Continue walking without interruption":
            H "I shouldn't overhear other people's conversations."
    $ add_note("Proceed - to continue as planned.")
    $ add_note("Firm - not soft, but not completely hard.")
    jump ch1_hub

label ch1_library_first:

    scene bg library with dissolve
    N "The library greeted me with the smell of old paper and polished mahogany. An open map of the area lay on the table next to an empty envelope."
    $ add_note("Mahogany - a dark, red-brown wood used to make furniture.")
    menu:
        "Where should I start?"
        "Examine the map":
            H "The routes to the village are clearly marked. A separate path indicates direct access to the hospital's pharmacy."
        "Inspect the envelope":
            H "It remains unmarked, it has only a printer's insignia. Someone removed its contents recently."
            jump ch1_library_first
        "Return to exploration":
            pass
    $ add_note("Inspect - to look at something very carefully.")
    jump ch1_hub

label ch1_guestroom_first:

    scene bg guestroom with dissolve
    N "The room was cozy: a warm light illuminated the room, a cup of freshly brewed coffee was steaming  on the writing desk, the bed was neatly made up and smelled fresh."
    $ add_note("Brew - If you brew tea or coffee, you make it by adding hot water, and if it brews, it gradually develops flavour in hot water.")
    menu:
        "What requires attention?"
        "Put my things away":
            H "A few shirts, a notebook, glasses and pajamas."
            jump ch1_guestroom_first
        "Observe through the window":
            H "A figure moved rapidly past the distant wing. Identification was impossible."
            jump ch1_guestroom_first
        "Resume exploration":
            pass
    $ add_note("Observe - to watch someone or something carefully.")
    $ add_note("Rapidly - happening or moving very quickly.")
    jump ch1_hub

# Evening of the 1st chapter
label ch1_evening:

    scene bg hall2 with fade
    stop music fadeout 0.6
    play music "audio/fireplace_evening.mp3" fadein 1.0

    N "By evening, all member of the family assembled near the fireplace. "
    show emily at center
    E "I have obligations in the village tomorrow. I hope everything will proceed efficiently."
    $ add_note ("Obligations - something that you do because it is your duty or because you feel you have to.")

    show john at left
    J "If you require transportation, just inform me."
    show alfred at right
    A "I'm sorry, I have to leave you, I have an appointment."
    hide alfred with dissolve
    hide emily with dissolve
    hide john with dissolve

    N "Although the conversation was conducted in formal politeness, there was doubt and wariness in the looks."
    stop music fadeout 1.0

    # Night
    scene bg guestroom_ev with dissolve
    play music "audio/night_creaks.mp3" fadein 0.8
    N "During the night's deepest hours, the atmosphere in the house changed. The initial rustle was replaced by distant urgent footsteps."
    menu:
        "Investigate the disturbance?"
        "Remain in bed":
            H "(Fatigue overwhelmed curiosity. Morning will clear everything up.)"
        "Go out into the corridor":
            scene bg corridor with dissolve
            N "Faint lamplight illuminated the hallway. A distant door's light flickered briefly before extinguishing."
    $ add_note("Investigate - to try to discover all the facts about something, especially a crime or accident.")
    $ add_note("Disturbance - something that interrupts what you are doing, especially something loud or annoying.")
    $ add_note("Fatigue - the feeling of being tired.")
    $ add_note("Overwhelmed - If a feeling or situation overwhelms someone, it has an effect that is too strong or extreme..")
    $ add_note("Curiosity - the feeling of wanting to know or learn about something.")
    $ add_note("Faint - slight and not easy to notice, smell, hear, etc.")
    $ add_note("Flicker - to shine with a light that is sometimes bright and sometimes weak.")
    $ add_note("Extinguish - to stop something burning or giving out light.")
    stop music fadeout 1.0

    N "Thus concluded my initial day at Styles Court."
    jump english_vocabulary_quiz

# ---------------------------------------------------------
# СИСТЕМА ТЕСТОВ ДЛЯ ИЗУЧЕНИЯ АНГЛИЙСКОГО
# ---------------------------------------------------------
default english_quiz_score = 0
default total_english_questions = 15

screen english_quiz_results():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        has vbox
        spacing 15
        
        label "Quiz Results" xalign 0.5
        
        if english_quiz_score >= 12:
            text "Excellent! You scored [english_quiz_score]/[total_english_questions]!" size 24 color "#00ff00" xalign 0.5
            text "Your English comprehension is outstanding!" size 18 xalign 0.5
        elif english_quiz_score >= 8:
            text "Good job! [english_quiz_score]/[total_english_questions]" size 24 color "#ffff00" xalign 0.5
            text "You have a solid understanding of the vocabulary." size 18 xalign 0.5
        else:
            text "Score: [english_quiz_score]/[total_english_questions]" size 24 color "#ff0000" xalign 0.5
            text "Keep practicing to improve your skills!" size 18 xalign 0.5
        
        textbutton "Continue":
            xalign 0.5
            action [Hide("english_quiz_results"), Return()]

label english_vocabulary_quiz:
    scene bg study with fade
    play music "audio/thinking.mp3" fadein 1.0
    
    show poirot at center
    P "Mon ami! Now we shall test your English comprehension. Let us begin with vocabulary!"
    
    $ english_quiz_score = 0
    
    # SECTION 1: VOCABULARY - MEANING OF WORDS (5 questions)
    P "First section: Vocabulary meaning. Choose the correct definition."
    
    # Question 1
    menu vocab1:
        P "What does 'initial' mean?"
        
        "Noisy and chaotic":
            P "Incorrect! Tranquil means first."
            
        "Earliest and first":
            P "Exactly correct! +1 point"
            $ english_quiz_score += 1
            
        "Dangerous and threatening":
            P "Non, initial describes happening at the beginning, not danger."
    
    # Question 2
    menu vocab2:
        P "What is the meaning of 'vibrant'?"
        
        "Dull and faded":
            P "No, that's the opposite meaning."
            
        "Full of excitement and energy":
            P "Perfect! You understand precisely. +1 point"
            $ english_quiz_score += 1
            
        "Quick and hurried":
            P "Incorrect! Vibrant means energetic."
    
    # Question 3  
    menu vocab3:
        P "Define 'brew' in the context of our story."
        
        "To make beer":
            P "No, you don't understand the meaning of the word."
            
        "If you brew tea or coffee, you make it by adding hot water, and if it brews, it gradually develops flavour in hot water.":
            P "Excellent deduction! +1 point"
            $ english_quiz_score += 1
            
        "A drink made by brewing, such as beer or tea":
            P "No, that's not the definition."
    
    # Question 4
    menu vocab4:
        P "What does 'fatigue' mean?"
        
        "Vigor and energy":
            P "Fatigue means the opposite of vigor."
            
        "The feeling of being tired":
            P "Precisely! You observe well. +1 point"
            $ english_quiz_score += 1
            
        "Anger and rage":
            P "Fatigue suggests tiredness, not anger."
    
    # Question 5
    menu vocab5:
        P "What is an 'estate' in our story?"
        
        "A small apartment":
            P "An estate is large, not small."
            
        "A large property with land":
            P "Correct! Styles is a country estate. +1 point"
            $ english_quiz_score += 1
            
        "A business in the city":
            P "An estate typically refers to a large rural property."
    
    # SECTION 2: GRAMMAR IN CONTEXT (5 questions)
    P "Now, grammar questions based on the story text."
    
    # Question 6 - Verb tenses
    menu grammar1:
        P "Complete this sentence correctly: 'The birds ___ singing and leaves ___ rustling.'"
        
        "are, are":
            P "Incorrect with plural subjects 'birds' and 'leaves'."
            
        "was, was":
            P "The subjects are plural, need plural verbs."
            
        "were, were":
            P "Perfect grammar! +1 point"
            $ english_quiz_score += 1
    
    # Question 7 - Prepositions
    menu grammar2:
        P "Choose the correct preposition: 'I had leisure time ___ dinner.'"
        
        "during":
            P "'Before' indicates time preceding dinner."
            
        "before":
            P "Excellent! The time was preceding dinner. +1 point"
            $ english_quiz_score += 1
            
        "while":
            P "'While' would mean during the dinner itself."
    
    # Question 8 - Word order
    menu grammar3:
        P "Which sentence has correct word order?"
        
        "A gravel path to the oak door led.":
            P "The word order is incorrect."
            
        "Led a gravel path to the oak door.":
            P "This is not a complete sentence with proper structure."
            
        "A gravel path led to the oak door.":
            P "Perfect English word order! +1 point"
            $ english_quiz_score += 1
    
    # Question 9 - Articles
    menu grammar4:
        P "Choose the correct article: 'There was ___ scent of polished oak.'"
        
        "a":
            P "Correct! We use 'a' with singular countable nouns. +1 point"
            $ english_quiz_score += 1
            
        "an":
            P "'Scent' begins with a consonant sound."
            
        "the":
            P "We use 'the' for specific, previously mentioned things."
    
    # Question 10 - Adjectives
    menu grammar5:
        P "Which adjective form is correct: 'The ___ mansion didn't attract much attention.'"
        
        "quiet":
            P "Excellent! 'Quiet' is the correct adjective form. +1 point"
            $ english_quiz_score += 1
            
        "quietly":
            P "'Quietly' would describe how something is done."
            
        "quietness":
            P "'Quietness' is a noun, not an adjective."
    
    # SECTION 3: COMPREHENSION AND USAGE (5 questions)
    P "Final section: Reading comprehension and word usage."
    
    # Question 11 - Context comprehension
    menu comprehension1:
        P "Based on the story, why might Alfred's politeness seem 'unnatural'?"
        
        "Because he's usually very rude":
            P "We only see his current behavior, not his usual manner."
            
        "Because it seems too measured and deliberate":
            P "Exactly! It seems excessively careful. +1 point"
            $ english_quiz_score += 1
            
        "Because he doesn't speak English well":
            P "No, his English seems fine."
    
    # Question 12 - Vocabulary in context
    menu comprehension2:
        P "When Cynthia says she can 'assist' at the pharmacy, what does she mean?"
        
        "Cause trouble":
            P "'Assist' means to help, not hinder."
            
        "Provide help":
            P "Correct! Assist means to help or aid. +1 point"
            $ english_quiz_score += 1
            
        "Steal medicines":
            P "No, that would be illegal!"
    
    # Question 13 - Multiple meaning words
    menu comprehension3:
        P "What does 'firm' mean in: 'The woman's voice remained firm'?"
        
        "Soft and gentle":
            P "Firm suggests strength, not softness."
            
        "Unchanging and determined":
            P "Exactly! Firm can mean resolute or determined. +1 point"
            $ english_quiz_score += 1
            
        "A business company":
            P "That's the noun form, here it's an adjective."
    
    # Question 14 - Synonyms
    menu comprehension4:
        P "Which word is a synonym for 'rapidly' as in 'moved rapidly'?"
        
        "Slowly":
            P "Slowly means the opposite of rapidly."
            
        "Quickly":
            P "Perfect! Rapidly and quickly are synonyms. +1 point"
            $ english_quiz_score += 1
            
        "Carefully":
            P "Carefully describes how, not how fast."
    
    # Question 15 - Word forms
    menu comprehension5:
        P "What is the noun form of 'acquired' as in 'recently acquired editions'?"
        
        "Acquisition":
            P "Excellent! Acquisition is the noun form. +1 point"
            $ english_quiz_score += 1
            
        "Acquiring":
            P "Acquiring is a verbal noun, but acquisition is better."
            
        "Acquire":
            P "That's the base verb, not the noun."
    
    # Show results
    call screen english_quiz_results
    hide screen english_quiz_results
    
    # Feedback based on score
    if english_quiz_score >= 12:
        P "Magnifique! Your English comprehension is exceptional! You have mastered both vocabulary and grammar."
        H "Thank you, Poirot! I've been studying diligently."
    elif english_quiz_score >= 8:
        P "Good work, my friend! You have a solid foundation in English. With more practice, you will excel."
        H "I'll continue to improve my skills."
    else:
        P "Do not be discouraged! Learning a language takes time. Review the vocabulary and try again."
        H "I'll study harder, Poirot."
    
    P "Remember these words - they are essential for understanding our investigation fully."
    
    stop music fadeout 1.0
    return

# Добавляем возможность запуска английского теста из меню
label start_english_quiz:
    scene black
    show text "English Vocabulary and Comprehension Test" at truecenter
    with fade
    pause 1.0
    hide text
    call english_vocabulary_quiz
    jump ch2_continue_investigation
