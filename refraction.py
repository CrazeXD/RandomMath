import math

def angle(index1, index2, incident):
    incident = incident
    incident = math.sin(incident)
    incident*=index1
    incident/=index2
    return incident

def index(index1, incident, refracted):
    indicent = incident
    incident = math.sin(incident)
    incident*=index1
    incident/=math.sin(refracted)
    return incident
