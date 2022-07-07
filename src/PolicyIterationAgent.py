from hashlib import new
import numpy as np
from agent import Agent


# TASK 1

class PolicyIterationAgent(Agent):

    def __init__(self, mdp, discount=0.9, iterations=100):
        """
        Your policy iteration agent take an mdp on
        construction, run the indicated number of iterations
        and then act according to the resulting policy.
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations

        states = self.mdp.getStates()
        number_states = len(states)
        # Policy initialization
        # ******************
        # TODO 1.1.a)
        # self.V = ...
        """
        states = [(-1,-1),(0,1),(0,2)......]
        """
        self.V={}
        for state in states:
            self.V.update({state:0})
        # *******************

        self.pi = {s: self.mdp.getPossibleActions(s)[-1] if self.mdp.getPossibleActions(s) else None for s in states}

        counter = 0

        start_counter = 0
        while True:
            # Policy evaluation
            for i in range(iterations):
                newV = {}
                for s in states:
                    a = self.pi[s]                 # give possible actions in state
                    # *****************
                    # TODO 1.1.b)
                    # if...
                    #
                    # else:...
                    # print("action: ",a)
                    
                    if a==None:
                        newV.update({s:0})
                    else:
                        next_statesAndProb_list = self.mdp.getTransitionStatesAndProbs(s, a)
                        reward = self.mdp.getReward(s, a, None)
                        temp = 0

                        for nxtstate, prob in next_statesAndProb_list:
                            temp += prob*(reward + self.discount*self.V[nxtstate])
                        newV.update({s:temp})

                # update value estimate
                # self.V=...
                # ******************
                for s in states:
                    self.V.update({s:newV[s]})
                

            policy_stable = True
            for s in states:
                actions = self.mdp.getPossibleActions(s)

                if len(actions) < 1:
                    self.pi[s] = None
                else:
                    old_action = self.pi[s]
                    # ************
                    # TODO 1.1.c)
                    # self.pi[s] = ...

                    # values_against_oldactions = np.zeros(len(old_action))
                    values_against_oldactions = np.zeros(len(actions))

                    #iterating over old actions
                    for j in range(len(actions)):
                        current_action = actions[j]
                        current_state = s
                        reward = self.mdp.getReward(current_state, current_action, None)
                        succ = self.mdp.getTransitionStatesAndProbs(current_state, current_action)

                        for nextstate, prob in succ:
                            values_against_oldactions[j] += prob*(reward + self.discount*self.V[nextstate])
                    
                    best_action_idx = np.argmax(values_against_oldactions)
                    self.pi.update({s:actions[best_action_idx]})

                    # policy_stable =

                    if(old_action!= self.pi[s]):
                        policy_stable = False
                    # ****************
                    
            counter += 1

            if policy_stable: break

        print("Policy converged after %i iterations of policy iteration" % counter) 


    def getValue(self, state):
        """
        Look up the value of the state (after the policy converged).
        """
        # *******
        # TODO 1.2.

        return self.V[state]

        # ********

    def getQValue(self, state, action):
        """
        Look up the q-value of the state action pair
        (after the indicated number of value iteration
        passes).  Note that policy iteration does not
        necessarily create this quantity and you may have
        to derive it on the fly.
        """
        # *********
        # TODO 1.3.

        succ = self.mdp.getTransitionStatesAndProbs(state, action)
        reward = self.mdp.getReward(state, action, None)

        temp = 0
        for nextstate, prob in succ:
            temp+=prob*(reward +self.discount*self.V[nextstate])
        
        return temp

        # **********

    def getPolicy(self, state):
        """
        Look up the policy's recommendation for the state
        (after the indicated number of value iteration passes).
        """
        # **********
        # TODO 1.4.

        return self.pi[state]

        # **********

    def getAction(self, state):
        """
        Return the action recommended by the policy.
        """
        return self.getPolicy(state)

    def update(self, state, action, nextState, reward):
        """
        Not used for policy iteration agents!
        """

        pass
