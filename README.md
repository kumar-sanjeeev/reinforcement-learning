<p align="center">
    <b>Reinforcement learning techniques</b>
</p>

Implemented the `VALUE ITERATION`, `POLICY ITERATION` and `Q LEARNING` on the grid World Environment.

### Table of content
* Getting Started
* Information about main code files
* Quick Start GridWorld
* Value Iteration Result
* Policy Iteration Result


#### Getting Started:
1. Clone the repo :
```shell
$ git clone https://github.com/kumar-sanjeeev/reinforcement-learning.git
```
2. Install the dependencies by running `requirements.txt` file
```shell
$ pip install -r requirements.txt
```

#### Information about main code files
* `agent.py`, `RandomAgent.py` : General class as template for agents and a completed RandomAgent
* `ValueIterationAgent.py`  : value iteration agent
* `PolicyIterationAgent.py` : policy iteration agent
* `QLearningAgent.py`       : q learning agent
* `output_xxx_selftest.txt` : output of specific runs to check your implementation
* `solution_xxx.py`         : result obtained
* `mdp.py`                  : abstract clas for general MDPs
* `environmrnt.py`          : abstract class for general reinforcement learning environments
* `gridworld.py`            : gridworld main code and test harness
* `gridworldclass.py`       : implementation of gridworld internals
* `utils.py`                : some utility code

#### Quick Start GridWorld
To get started run the gridworld in interactive mode:
* move the agent with arrow keys
```shell
python3 gridworld.py -m
```
![image](https://user-images.githubusercontent.com/62834697/177839894-fdce24fc-e0ec-43d8-a102-e36c67bf8935.png)

Control the different aspects of the simulation. A full list is available by running:
```shell
python3 gridworld.py -h
```

```
Options:
  -h, --help            show this help message and exit
  -d DISCOUNT, --discount=DISCOUNT
                        Discount on future (default 0.9)
  -r R, --livingReward=R
                        Reward for living for a time step (default 0.0)
  -n P, --noise=P       How often action results in unintended direction
                        (default 0.2)
  -e E, --epsilon=E     Chance of taking a random action in q-learning
                        (default 0.3)
  -l P, --learningRate=P
                        TD learning rate (default 0.5)
  -i K, --iterations=K  Number of rounds of policy evaluation or value
                        iteration (default 10)
  -k K, --episodes=K    Number of epsiodes of the MDP to run (default 0)
  -g G, --grid=G        Grid to use (case sensitive; options are BookGrid,
                        BridgeGrid, CliffGrid, MazeGrid, CustomGrid, default
                        BookGrid)
  -w X, --windowSize=X  Request a window width of X pixels *per grid cell*
                        (default 150)
  -a A, --agent=A       Agent type (options are 'random', 'value' ,
                        'policyiter' and 'q', default random)
  -t, --text            Use text-only ASCII display
  -p, --pause           Pause GUI after each time step when running the MDP
  -q, --quiet           Skip display of any learning episodes
  -s S, --speed=S       Speed of animation, S > 1.0 is faster, 0.0 < S < 1.0
                        is slower (default 1.0)
  -m, --manual          Manually control agent (for lecture)

```

