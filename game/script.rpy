
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

# VOCABULARY B2 LEVEL:
# tranquil - peaceful, calm
# estate - large property with land
# facade - front exterior of a building
# meticulous - showing great attention to detail
# restrained - controlled, not showing emotion
# withdrawn - shy, quiet, not communicative
# ambiguous - unclear, able to be interpreted multiple ways
# residue - remaining traces of something
# methodical - systematic, orderly
# superficial - on the surface, not deep
# inheritance - property received from someone who has died
# coincidence - chance occurrence of events
# speculation - forming theories without firm evidence
  
# inding
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
#

# ---------------------------------------------------------
# ГЛАВА 1 — ПРИБЫТИЕ В СТАЙЛЗ
# ---------------------------------------------------------
label start:

    scene bg exterior_day with fade
    play music "audio/strings_manor_day.mp3" fadein 1.2

    N "On a bright afternoon, the winding road led me to Styles Court, a quiet mansion which didn't attract much attention. The facade looked welcoming — ivy embraced the walls, a gravel path led to the oak door, sunlight reflected on the windows."
    $ add_note ("I have arrived at Styles, the country estate of the Cavendish family.")

    show john at right
    J "Hastings! Long time no see, we missed London's news."
    H "John, glad to see you again. Everything appears unchanged here... at first sight."
    $ add_note("The host is John Cavendish, an old friend of mine.")

    N "There was the scent of polished oak and fresh flowers in the hall. A servant took my luggage to the house."

    scene bg hall with dissolve
    show dorkas at center
    S "Your belongings will be delivered to your room momentarily, sir." 
    H "Thank you, I appreciate your assistance."
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
    $ add_note("Emily Inglethorp manages the household with notable energy and attention.")
    $ add_clue("emily_rules_home", "Emily maintains absolute control over domestic affairs and finances.")
    hide emily with dissolve
    menu:
        "Continue making acquaintances"
        "Introduce myself to Alfred":
            jump ch1_meet_alfred
        "Engage John and Mary in conversation":
            jump ch1_meet_mary
        "Request permission to examine the library":
            jump ch1_free_roam_intro

label ch1_meet_alfred:

    show alfred at right
    A "A pleasure to make your acquaintance. We value precision and routine here, and I hope you'll appreciate these qualities."
    H "Of course, I will respect both the customs and the rules of this house."
    $ add_note("Alfred Inglethorp, Emily's considerably younger husband, demonstrates meticulously polite behavior.")
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
    hide alfred with dissolve
    jump ch1_meet_mary

label ch1_meet_john:

    show john at right
    J "The family maintains appearances, though everyone has their own concerns. As expected, my mother remains active."
    H "This shows that the household continues its vibrant activity."
    $ add_note("John seems reluctant to elaborate on family matters.")
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
    $ add_note("Mary demonstrates perceptive intelligence and maintains dignified composure.")
    
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
    C "Good afternoon! I frequently assist at the village dispensary — should you require any medicinal preparations, I can recommend reliable sources."
    H "I hope circumstances won't necessitate them, but the information is valuable regardless."
    $ add_note("Cynthia, under Emily's guardianship, works at the village pharmacy.")
    hide cynthia with dissolve
    jump ch1_branch_more_people

label ch1_meet_lawrence:

    hide mary with dissolve
    show lawrence at left
    L "Your timing is fortuitous — the library has recently acquired several rare editions."
    H "That sounds particularly intriguing."
    $ add_note("Lawrence, the younger son, appears introverted and somewhat withdrawn.")
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
        "Conclude introductions — commence exploration":
            jump ch1_free_roam_intro

# Free overview of locations 
label ch1_free_roam_intro:

    N "I had leisure before the evening meal. The house itself seemed to invite systematic exploration."
    $ add_note("Initial exploration: garden, library, guest chamber.")
    jump ch1_hub

label ch1_hub:

    menu:
        "Which area warrants investigation?"
        "Garden — pathways, hedges, summerhouse":
            jump ch1_garden_first
        "Library — documents, correspondence, volumes":
            jump ch1_library_first
        "Guest chamber — settle belongings":
            jump ch1_guestroom_first
        "Join the gathering — evening assembly in the hall":
            jump ch1_evening

label ch1_garden_first:

    scene bg garden with dissolve
    N "The garden's foliage whispered like conspirators exchanging secrets. Muffled voices carried from a distant arbor."
    menu:
        "How should I proceed?"
        "Approach discreetly to overhear":
            H " (The discussion involved tense exchanges. A feminine voice maintained firmness, while the masculine response seemed deliberately ambiguous.)"
            $ add_note("Witnessed a strained conversation in the garden — specific content remained indistinct.")
            $ suspicion["Alfred"] += 1
        "Continue walking without interruption":
            H "For now, I remain a guest rather than an investigator."
    jump ch1_hub

label ch1_library_first:

    scene bg library with dissolve
    N "The library greeted me with the distinctive scent of aged paper and polished mahogany. A local map lay unfolded on the desk beside an empty envelope."
    menu:
        "What merits examination?"
        "Survey the map":
            H "The routes to the village are clearly marked. A separate path indicates direct access to the dispensary."
            $ add_clue("map_pharmacy", "The map highlights a footpath leading directly to the village pharmacy.")
            jump ch1_library_first
        "Inspect the envelope":
            H "It remains unmarked, bearing only a printer's insignia. Someone removed its contents recently."
            $ add_clue("blank_envelope", "Empty envelopes with distinctive printing are available in the house.")
            jump ch1_library_first
        "Return to exploration":
            pass
    jump ch1_hub

label ch1_guestroom_first:

    scene bg guestroom with dissolve
    N "The chamber offered comfortable accommodation: garden views, a traveling trunk, and a writing desk."
    menu:
        "What requires attention?"
        "Organize my possessions":
            H "Several shirts, a notebook for observations — the latter will prove essential."
            $ add_note("I've prepared a notebook for recording significant details.")
            jump ch1_guestroom_first
        "Observe through the window":
            H "A figure moved rapidly past the distant wing. Identification proved impossible."
            $ add_note("Observed an unidentified individual hurrying toward the remote wing.")
            jump ch1_guestroom_first
        "Resume exploration":
            pass
    jump ch1_hub

# Evening of the 1st chapter
label ch1_evening:

    scene bg hall2 with fade
    stop music fadeout 0.6
    play music "audio/fireplace_evening.mp3" fadein 1.0

    N "By evening, the household assembled near the fireplace. Light and shadow danced across the walls as if the mansion itself listened intently."
    show emily at center
    E "I have obligations in the village tomorrow. I anticipate everything will proceed efficiently."
    $ add_note ("The lady of the house plans a village excursion tomorrow.")

    show john at left
    J "Should you require transportation, simply inform me."
    show alfred at right
    A "Regrettably, correspondence demands my attention."
    hide alfred with dissolve
    hide emily with dissolve
    hide john with dissolve

    N "The conversation maintained perfect civility; the exchanged glances conveyed different messages entirely."
    stop music fadeout 1.0

    # Night
    scene bg guestroom_ev with dissolve
    play music "audio/night_creaks.mp3" fadein 0.8
    N "During the night's deepest hours, the house's acoustics transformed. Initial rustling yielded to distant, urgent footsteps."
    menu:
        "Investigate the disturbance?"
        "Remain in bed":
            H "(Fatigue overwhelmed curiosity. Morning will provide clarification.)"
        "Venture into the corridor":
            scene bg corridor with dissolve
            N "Faint lamplight illuminated the hallway. A distant door's light flickered briefly before extinguishing."
            $ add_note("Someone maintained nocturnal activity in the remote wing.")
    stop music fadeout 1.0

    N "Thus concluded my initial day at Styles Court."
    jump vocabulary_quiz

label vocabulary_quiz:
    scene bg library with fade
    play music "audio/thinking.mp3" fadein 1.0
    
    show poirot at center
    P "Mon ami! Before we continue our investigation, let us test your comprehension of the situation. Answer these questions to demonstrate your analytical abilities."
    
    $ quiz_score = 0
    $ total_questions = 5
    
    # Question 1 - Vocabulary
    menu quiz_question1:
        P "First question: What does the word 'tranquil' mean in the context of the estate's description?"
        
        "Noisy and busy":
            H "I don't think that's right..."
            P "Incorrect, my friend. The estate was described as peaceful, not noisy."
            
        "Peaceful and calm":
            H "Yes, the estate appeared calm and peaceful."
            P "Exactly! 'Tranquil' means peaceful and calm. +1 point for your observation."
            $ quiz_score += 1
            
        "Dangerous and threatening":
            H "That doesn't seem accurate."
            P "Non, the facade was welcoming, not threatening."
    
    # Question 2 - Plot comprehension
    menu quiz_question2:
        P "Second question: What was Hastings' initial impression of Alfred Inglethorp?"
        
        "Warm and friendly":
            H "No, he was quite formal actually."
            P "His politeness lacked genuine warmth, you recall."
            
        "Meticulously polite and reserved":
            H "Yes, he was very formal and measured in his speech."
            P "Precisely! He demonstrated meticulously polite behavior. +1 point."
            $ quiz_score += 1
            
        "Angry and confrontational":
            H "No, he was quite controlled."
            P "He was restrained, not confrontational."
    
    # Question 3 - Vocabulary in context
    menu quiz_question3:
        P "Third question: When we found 'residue' in the cup, what were we referring to?"
        
        "The cup itself":
            H "No, it was something inside the cup."
            P "The residue was inside the cup, not the cup itself."
            
        "Remaining traces of liquid":
            H "Yes, the leftover substance in the cup."
            P "Correct! Residue means remaining traces of something. +1 point."
            $ quiz_score += 1
            
        "The cup's design":
            H "That doesn't make sense in context."
            P "We were examining the contents, not the design."
    
    # Question 4 - Character analysis
    menu quiz_question4:
        P "Fourth question: How would you describe Lawrence Cavendish's personality based on our observations?"
        
        "Outgoing and sociable":
            H "No, he seemed quite the opposite."
            P "He was not particularly sociable, you recall."
            
        "Introverted and withdrawn":
            H "Yes, he appeared quiet and reserved."
            P "Exactly! He appeared introverted and somewhat withdrawn. +1 point."
            $ quiz_score += 1
            
        "Suspicious and dangerous":
            H "We shouldn't jump to conclusions."
            P "We have no evidence to suggest he is dangerous."
    
    # Question 5 - Vocabulary application
    menu quiz_question5:
        P "Final question: What does 'methodical' mean in the context of our investigation?"
        
        "Random and chaotic":
            H "No, that's the opposite of how we work."
            P "Our approach is systematic, not chaotic."
            
        "Slow and inefficient":
            H "No, being methodical doesn't mean being slow."
            P "Methodical means orderly and systematic, not necessarily slow."
            
        "Systematic and orderly":
            H "Yes, we follow a careful, step-by-step process."
            P "Perfect! Methodical means systematic and orderly. +1 point."
            $ quiz_score += 1
    
    # Quiz results
    hide poirot
    show poirot at center
    if quiz_score == total_questions:
        P "Magnifique! You scored [quiz_score] out of [total_questions]! Your comprehension is excellent, mon ami. You notice the important details."
        H "Thank you, Poirot. I'm trying to be as observant as you."
        
    elif quiz_score >= 3:
        P "Not bad, my friend. [quiz_score] out of [total_questions] - you have a good eye for details, but there is room for improvement."
        H "I'll continue to develop my observational skills."
        
    else:
        P "Hmm, [quiz_score] out of [total_questions]. We must work on your attention to detail. The little grey cells need more exercise!"
        H "I'll study more carefully, Poirot."
    
    # Vocabulary review
    P "Let us review the key vocabulary from our investigation:"
    show screen vocabulary_review
    pause
    hide screen vocabulary_review
    
    P "Now, let us return to our investigation. Remember these words - they may prove crucial to solving our mystery."
    
    stop music fadeout 1.0
    jump start_quiz_from_menu

screen vocabulary_review():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        has vbox
        spacing 10
        
        label "Vocabulary Review" xalign 0.5
        text "tranquil - peaceful, calm" size 18
        text "estate - large property with land" size 18
        text "facade - front exterior appearance" size 18
        text "meticulous - showing great attention to detail" size 18
        text "residue - remaining traces of something" size 18
        text "methodical - systematic, orderly" size 18
        text "withdrawn - shy, quiet, not communicative" size 18
        text "inheritance - property received after someone's death" size 18
        
        textbutton "Continue":
            xalign 0.5
            action Hide("vocabulary_review")

# Добавляем возможность запуска квиза из главного меню или в процессе игры
label start_quiz_from_menu:
    scene black
    show text "Vocabulary and Comprehension Quiz" at truecenter
    with fade
    pause 1.0
    hide text
    jump vocabulary_quiz

# Вставляем точку продолжения после квиза
label ch2_continue_investigation:
    scene bg hall with fade
    show poirot at center
    P "Now, where were we? Ah yes, the investigation continues..."
    # Продолжение основной игры

