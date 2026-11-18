
EMOTIONS = {
    'sad': {
        '15-20': [
            'Watch a comedy movie',
            'Play video games',
            'Chat with friends online'
        ],
        '20-25': [
            'Hear some uplifting music',
            'Try a new workout or dance class',
            'Catch up with an old friend'
        ],
        '25-30': [
            'Try cooking a new recipe',
            'Watch a stand-up comedy show',
            'Read an inspirational book'
        ],
        '30-35': [
            'Take a short trip',
            'Watch a favorite comedy movie',
            'Practice meditation or yoga'
        ],
        '35-40': [
            'Spend time with family or friends',
            'Enjoy a good comedy book',
            'Try a fun hobby like painting'
        ],
        '40+': [
            'Visit a local theater or comedy show',
            'Go out for dinner',
            'Reconnect with an old friend or relative'
        ]
    },
    'surprise': {
        '15-20': [
            'Dance to your favorite music',
            'Call a close friend',
        ],
        '20-25': [
            'Plan an impromptu gathering',
            'Listen to some energizing music'
        ],
        '25-30': [
            'Capture the moment with photos',
            'Celebrate with family'
        ],
        '30-35': [
            'Take a spontaneous drive',
            'Watch a feel-good movie'
        ],
        '35-40': [
            'Celebrate with family',
            'Go for a nature walk'
        ],
        '40+': [
            'Reflect on the surprise with loved ones',
            'Enjoy a quiet moment with music'
        ]
    },
    'neutral': {
        '15-20': [
            'Explore a new hobby',
            'Watch a trending movie',
        ],
        '20-25': [
            'Try a meditation session',
            'Have a chat with someone close'
        ],
        '25-30': [
            'Relax with a good book',
            'Try a new recipe'
        ],
        '30-35': [
            'Catch up on some reading',
            'Watch a light-hearted movie'
        ],
        '35-40': [
            'Plan for the week ahead',
            'Listen to some relaxing music'
        ],
        '40+': [
            'Go for a peaceful walk',
            'Enjoy time with loved ones'
        ]
    },
    'happy': {
        '15-20': [
            'Watch an action movie',
            'Play a favorite sport',
            'Go out with friends'
        ],
        '20-25': [
            'Celebrate with friends',
            'Plan a weekend trip'
        ],
        '25-30': [
            'Have a family gathering',
            'Try an outdoor adventure'
        ],
        '30-35': [
            'Have a family movie night',
            'Cook a favorite dish'
        ],
        '35-40': [
            'Take a scenic drive',
            'Celebrate with family'
        ],
        '40+': [
            'Enjoy a quiet evening with family',
            'Visit a favorite restaurant'
        ]
    },
    'fear': {
        '15-20': [
            'Sit with someone you trust',
            'Watch a light-hearted movie'
        ],
        '20-25': [
            'Listen to calming music',
            'Try a relaxation app'
        ],
        '25-30': [
            'Practice breathing exercises',
            'Go for a gentle walk'
        ],
        '30-35': [
            'Spend time with family',
            'Listen to soothing music'
        ],
        '35-40': [
            'Share your thoughts with someone close',
            'Practice meditation'
        ],
        '40+': [
            'Reflect with someone you trust',
            'Read an inspiring book'
        ]
    },
    'disgust': {
        '15-20': [
            'Read a fun book',
            'Spend time with pets'
        ],
        '20-25': [
            'Visit a new place',
            'Watch a favorite series'
        ],
        '25-30': [
            'Clean and organize a room',
            'Take a nature walk'
        ],
        '30-35': [
            'Read an uplifting book',
            'Visit a friend'
        ],
        '35-40': [
            'Go to a new restaurant',
            'Do a relaxing activity'
        ],
        '40+': [
            'Try a new hobby',
            'Spend quality time with family'
        ]
    },
    'angry': {
        '15-20': [
            'Go for a run or jog',
            'Play a sport'
        ],
        '20-25': [
            'Try a quick workout',
            'Listen to calming music'
        ],
        '25-30': [
            'Go for a walk in the park',
            'Take deep breaths'
        ],
        '30-35': [
            'Do light stretching',
            'Spend time outdoors'
        ],
        '35-40': [
            'Read a book',
            'Take a walk in nature'
        ],
        '40+': [
            'Practice deep breathing exercises',
            'Reflect on positive memories'
        ]
    }
}


def get_age( age):
   
    if age <= 20:
        age_range = '15-20'
    elif age <= 25:
        age_range = '20-25'
    elif age <= 30:
        age_range = '25-30'
    elif age <= 35:
        age_range = '30-35'
    elif age <= 40:
        age_range = '35-40'
    else:
        age_range = '40+'
    
    return age_range

