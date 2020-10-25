import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def createPitch():

#Create figure
    fig=plt.figure(facecolor='green')
    ax=fig.add_subplot(1,1,1)

    #Pitch Outline & Centre Line
    # List one: starting and ending X locations
    # List two: starting and ending Y locations
    plt.plot([0,0],[0,90], color="white") # plot ---  x y(0,0),x y - (0,90)
    plt.plot([0,130],[90,90], color="white")# plot ---  x y -(0,90), x y - (130,90)
    plt.plot([130,130],[90,0], color="white")# plot ---  x y -(130,90), x y - (130,0)
    plt.plot([130,0],[0,0], color="white")
    plt.plot([65,65],[0,90], color="white")
    
    #Left Penalty Area
    plt.plot([16.5,16.5],[65,25],color="white")
    plt.plot([0,16.5],[65,65],color="white")
    plt.plot([16.5,0],[25,25],color="white")
    
    #Right Penalty Area
    plt.plot([130,113.5],[65,65],color="white")
    plt.plot([113.5,113.5],[65,25],color="white")
    plt.plot([113.5,130],[25,25],color="white")
    
    #Left 6-yard Box
    plt.plot([0,5.5],[54,54],color="white")
    plt.plot([5.5,5.5],[54,36],color="white")
    plt.plot([5.5,0.5],[36,36],color="white")
    
    #Right 6-yard Box
    plt.plot([130,124.5],[54,54],color="white")
    plt.plot([124.5,124.5],[54,36],color="white")
    plt.plot([124.5,130],[36,36],color="white")

    # Left goal post
    plt.plot([0,-4.5],[49.5,49.5],color="white")
    plt.plot([-4.5,-4.5],[49.5,40.5],color="white")
    plt.plot([-4.5,0],[40.5,40.5],color="white")

    # Right goal post
    plt.plot([130,134],[49.5,49.5],color="white")
    plt.plot([134,134],[49.5,40.5],color="white")
    plt.plot([134,130],[40.5,40.5],color="white")

    
    #Assign circles to variables - do not fill the centre circle!
    centreCircle = plt.Circle((65,45),9.15,color="white",fill=False)
    centreSpot = plt.Circle((65,45),0.8,color="white")
    leftPenSpot = plt.Circle((11,45),0.8,color="white")
    rightPenSpot = plt.Circle((119,45),0.8,color="white")
    
    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)
    
    #Prepare Arcs
    leftArc = Arc((11,45),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="white")
    rightArc = Arc((119,45),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="white")

    #Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)
    
    #Tidy Axes
    plt.axis('off')
    
    #Display Pitch
    plt.show()
    
createPitch()
