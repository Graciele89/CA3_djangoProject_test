from django import forms

exercise_type = [('BENCH PRESS', 'Bench Press'), ('SQUAT', 'Squat'), ('DEADLIFT', 'Deadlift'), ('BARBELL ROW', 'Barbell Row'), ('OVERHEAD PRESS', 'Overhead Press'),
('DUMBBELL PRESS', 'Dumbbell Press'), ('DUMBBELL ROW', 'Dumbbell Row'), ('DUMBBELL CURL', 'Dumbbell Curl'), ('DUMBBELL FLY', 'Dumbbell Fly'),
('LAT PULLDOWN', 'Lat Pulldown'), ('PULL UP', 'Pull Up'), ('CHIN UP', 'Chin Up'), ('LEG PRESS', 'Leg Press'), ('LEG CURL', 'Leg Curl'),
('LEG EXTENSION', 'Leg Extension'), ('CALF RAISE', 'Calf Raise'), ('CRUNCH', 'Crunch'), ('PLANK', 'Plank'), ('RUSSIAN TWIST', 'Russian Twist'),
('HAMMER CURL', 'Hammer Curl'), ('TRICEPS EXTENSION', 'Triceps Extension'), ('CABLE CURL', 'Cable Curl'), ('CABLE FLY', 'Cable Fly'),
('CABLE ROW', 'Cable Row'), ('PUSH UP', 'Push Up'), ('DIP', 'Dip'), ('KETTLEBELL SWING', 'Kettlebell Swing'), ('BOX JUMP', 'Box Jump'),
('BURPEE', 'Burpee'), ('LUNGE', 'Lunge'), ('STEP UP', 'Step Up'), ('BATTLE ROPE', 'Battle Rope'), ('ROWING MACHINE', 'Rowing Machine'),
('YOGA', 'Yoga'), ('PILATES', 'Pilates'), ('ZUMBA', 'Zumba'), ('AEROBICS', 'Aerobics'), ('SPIN CLASS', 'Spin Class'), ('KICKBOXING', 'Kickboxing'),
('BOOT CAMP', 'Boot Camp'), ('HIIT', 'HIIT'), ('CIRCUIT TRAINING', 'Circuit Training'), ('STRENGTH TRAINING', 'Strength Training'),
('FUNCTIONAL TRAINING', 'Functional Training'), ('GROUP FITNESS CLASS', 'Group Fitness Class'), ('DANCE CLASS', 'Dance Class'),
('BODY PUMP', 'Body Pump'), ('BODY COMBAT', 'Body Combat'), ('BODY BALANCE', 'Body Balance'), ('BODY ATTACK', 'Body Attack')]

workout_plan = [('3 x 10 reps', 'Easy'), ('3 x 15 reps', 'Moderate'), ('4 x 15', 'Intense'), ('5 x 15', 'Insane')]
# ('EVERY DAY PLAN', [('DRINK WATER', 'Drink plenty of water'), ('WARM UP', 'Warm up for 5 min before exercising'), ('BREATHING EXERCISE 2 MIN', 'Breathing exercise for two minutos at the end')]),
# ('BEGINNER FULL BODY WORKOUT', [('SQUAT', 3, 12), ('BENCH PRESS', 3, 12), ('DUMBBELL ROW', 3, 12), ('LAT PULLDOWN', 3, 12), ('DUMBBELL CURL', 3, 12), ('TRICEPS EXTENSION', 3, 12)]),
# ('INTERMEDIATE UPPER BODY WORKOUT', [('BENCH PRESS', 3, 8), ('BARBELL ROW', 3, 8), ('OVERHEAD PRESS', 3, 8), ('DUMBBELL CURL', 3, 12), ('TRICEPS EXTENSION', 3, 12)]),
# ('ADVANCED LEG DAY WORKOUT', [('SQUAT', 5, 5), ('DEADLIFT', 5, 5), ('LEG PRESS', 3, 10), ('LEG CURL', 3, 10), ('CALF RAISE', 3, 15)]),
# ('BEGINNER CARDIO WORKOUT', [('TREADMILL', 20), ('STATIONARY BIKE', 15), ('ELLIPTICAL', 15), ('ROWING MACHINE', 10)]),
# ('INTERMEDIATE HIGH-INTENSITY INTERVAL TRAINING (HIIT)', [('SPRINTING', 30), ('REST', 30), ('JUMPING JACKS', 30), ('REST', 30), ('MOUNTAIN CLIMBERS', 30), ('REST', 30), ('BURPEES', 30), ('REST', 30), ('REPEAT 3-5 TIMES')]),
# ('ADVANCED FULL BODY CIRCUIT TRAINING', [('BURPEES', 1, 60), ('PULL UPS', 1, 10), ('PUSH UPS', 1, 20), ('KETTLEBELL SWINGS', 1, 20), ('SQUATS', 1, 20), ('DUMBBELL ROW', 1, 20), ('LUNGES', 1, 20), ('CRUNCHES', 1, 20), ('REST', 60), ('REPEAT 3-5 TIMES')]),
# ('BEGINNER PILATES WORKOUT', [('ROLL-UP', 3, 10), ('PILATES 100', 3, 10), ('LEG CIRCLES', 3, 10), ('THE HUNDRED', 3, 10),('ROLLING LIKE A BALL', 3, 10), ('SWAN DIVE', 3, 10)]),
# ('INTERMEDIATE PILATES WORKOUT', [('TEASER', 3, 8), ('CORKSCREW', 3, 8), ('SINGLE-LEG STRETCH', 3, 10), ('DOUBLE-LEG STRETCH', 3, 10), ('CRISS-CROSS', 3, 10), ('SWAN DIVE', 3, 10)]),
# ('ADVANCED PILATES WORKOUT', [('ROLL OVER', 3, 5), ('CONTROL BALANCE', 3, 5), ('THE CORKSCREW', 3, 5), ('CONTROLLED BALANCE OFF THE END', 3, 5),('TEASER ON THE WUNDA CHAIR', 3, 5), ('SWAN DIVE', 3, 10)]),
# ('BEGINNER YOGA WORKOUT', [('MOUNTAIN POSE', 5), ('TREE POSE', 5), ('CAT-COW STRETCH', 5), ('DOWNWARD-FACING DOG', 5), ('PLANK POSE', 5)]),
# ('INTERMEDIATE YOGA WORKOUT', [('WARRIOR I', 5), ('WARRIOR II', 5), ('TRIANGLE POSE', 5), ('CHILDS POSE', 5), ('UPWARD-FACING DOG', 5)]),
# ('ADVANCED YOGA WORKOUT', [('CROW POSE', 5), ('HEADSTAND', 5), ('FOREARM STAND', 5), ('WHEEL POSE', 5), ('PLANK TO CHATURANGA TO UPWARD-FACING DOG TO DOWNWARD-FACING DOG', 5)])


week_days = [('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday'), ('EVERY DAY', 'Every Day' )]


class PostFormExercise(forms.Form):

    text_exercise_type = forms.ChoiceField(label="Enter exercise type:", choices=exercise_type)
    text_workout_plan = forms.ChoiceField(label="Enter your workout plan:", choices=workout_plan)
    text_week_day = forms.ChoiceField(label=" Week Day:", choices=week_days)
    text_time = forms.CharField(label="Desired Time", widget=forms.TextInput(attrs={'type': 'time'}))
