import numpy as np

import util
from agent import Agent


# TASK 3

class QLearningAgent(Agent):
    def __init__(self, actionFunction, discount=0.9, learningRate=0.1, epsilon=0.3):
        """ A Q-Learning agent gets nothing about the mdp on construction other than a function mapping states to
        actions. The other parameters govern its exploration strategy and learning rate. """
        self.setLearningRate(learningRate)
        self.setEpsilon(epsilon)
        self.setDiscount(discount)
        self.actionFunction = actionFunction

        self.qInitValue = 0  # initial value for states
        self.Q = {}

    def setLearningRate(self, learningRate):
        self.learningRate = learningRate

    def setEpsilon(self, epsilon):
        self.epsilon = epsilon

    def setDiscount(self, discount):
        self.discount = discount

    def getValue(self, state):
        """ Look up the current value of the state. """
        # *********
        # TODO 3.1.
        if state not in self.Q.keys():
            return self.qInitValue
        else:    
            temp = self.Q[state].values()
            return max(temp)
        # *********

    def getQValue(self, state, action):
        """ Look up the current q-value of the state action pair. """
        # *********
        # TODO 3.2.
        if state not in self.Q.keys():
            return self.qInitValue 
        else:
            if action not in self.Q[state].keys():
                return self.qInitValue  
            else: 
                return self.Q[state][action]
        # *********

    def getPolicy(self, state):
        """ Look up the current recommendation for the state. """
        # *********
        # TODO 3.3.
        if state not in self.Q.keys():
            return self.getRandomAction(state)
        else:
            temp = self.Q[state]
            return max(temp,key=temp.get) 
        # *********

    def getRandomAction(self, state):
        all_actions = self.actionFunction(state)
        if len(all_actions) > 0:
            # *********
            return np.random.choice(all_actions)
            # *********
        else:
            return "exit"

    def getAction(self, state):
        """ Choose an action: this will require that your agent balance exploration and exploitation as appropriate. """
        # *********
        # TODO 3.4.
        if state not in self.Q.keys():
            return self.getRandomAction(state)
        else:
            length = len(self.Q[state].keys())
            if np.random.rand()>1-self.epsilon+self.epsilon/length :
                return self.getRandomAction(state)              
            else :
                return self.getPolicy(state)           
        # *********

    def update(self, state, action, nextState, reward):
        """ Update parameters in response to the observed transition. """
        # *********
        # TODO 3.5.
        if state not in self.Q.keys():
            all_actions = self.actionFunction(state)
            if len(all_actions)>0:
            # print("state,allaction",state,all_actions)
                for a in all_actions:
                    self.Q.update({state:{a:self.qInitValue}})
        # if nextState not in self.Q.keys():
        #     all_actions = self.actionFunction(nextState)
        #     if len(all_actions)>0:
        #     # print("state,allaction",state,all_actions)
        #         for a in all_actions:
        #             self.Q.update({nextState:{a:self.qInitValue}})

        self.Q[state][action] = (1-self.learningRate)*self.getQValue(state,action) + \
                                 self.learningRate*(reward+self.discount*self.getValue(nextState))
        # print("Q\n",self.Q)
        # print("\n")
        # # *********
