import yaml

configGroups = []
radioBttns = []

with open('config.yaml') as file:
    modules = yaml.load(file, Loader=yaml.FullLoader)
    iteration = 0
    rank_in_grp=0
    for module in modules.items():
        #print(module, ':', packages
        #makes a group for the currebnt module
        self.group = QtWidgets.QGroupBox(self.ui.centralwidget)
        self.group.setObjectName(module[1]["variable"]) #sets the objects name to be the name module
           
        if(iteration == 0):
            #first group added to row 0 col 0
            self.ui.gridLayout.addWidget(self.group, 0, 0)
        else:
            #all other groups added to row 1 and then the next open col
            self.ui.gridLayout.addWidget(self.group, 1, iteration-1)

            self.group.setTitle(module[0]) #sets the title in the UI
            #each group gets its own form layout that the bttns are added to
            self.formLayout = QtWidgets.QFormLayout(self.group)
            self.formLayout.setObjectName("formLayout_" + module)
            
        print(module)
        configGroups.append(list()) #makes the array for the groupping
    
        for choice in module[1]["choices"].items():
            #print(choice[0]) var name of choice
            #print(choice[1]["title"]) title of var thats seen in the GUI
            radioBttns.append(choice[0]) # an array to keep track of the bttns
            configGroups[iteration].append(choice[0]) #add bttns to thier groups
            #create the button
            self.bttn = QtWidgets.QRadioButton(self.group)
            self.bttn.setObjectName(choice[0]) #this is the name we use to access the object
            self.bttn.setText(choice[1]["title"]) #the text seen in the GUI
            self.formLayout.addWidget(self.bttn) #add the button to the layout
            #connect onclicked function to the button
            self.bttn.clicked.connect(partial(self.saveSelectedOptions,choice[0],iteration,rank_in_grp))
            rank_in_grp+=1
        iteration+=1

#test arrays
print(configGroups)
print(radioBttns)