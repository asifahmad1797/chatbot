import random

EATING = "I survive on electricity"
ADVICE = "Srinivas sir advice is like compass which navigate us through challeging situation"
COMPANY = "AdaInsys"
chet="chetana is is is ...... i think girl"
sah="sahil is ui/ux developer in adaInsys"
asi="Asif is developer in adaInsys"
sri="Mr Srinivas is the director of AdaInsys and my owner"
def unknown():

    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
