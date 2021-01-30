# Q-learning & Q-value iteration algorithms for the Block World Environment

## Motivation
This is the implementation of the Reinforcement Learning homework for the Machine Learning class at the School of Electrical Engineering, University of Belgrade.

## Block World environment
The environment originates from the book by [Russel & Norvig](http://aima.cs.berkeley.edu/). 

<img src="imgs/block_wrld.png"/>

Green and red fields are terminal states. Green field represents victory and it's reward is **+1**, while the red one represents defeat and it's reward is **-1**. <br/>
For each move the agent performs, it receives a small reward of: **-0.04**. The black field represents a wall. If the agent tries to go into that field or outside of the borders of the world it will remain in the same position/field.

## Q-value iteration algorithm
### Slip probability
When the agent decides to perform a certain action there is some probability that the agent will slip an end up in some other state. More specifically, when agent slips it can end up going in one of the directions which are orthogonal to the target one. Example: Agent wants to go to the ease, but can end up going to the north or south.
<br/>
Bellow you can see some analysis related to this subject. In this analysis a discount factor of 0.9 was used.

#### Slip probability=0.2
In this case agent goes to the target direction with probability of 0.8, but goes in orthogonal directions with probability 0.2 (0.1 each).
<br/>
The algorithm converges after 17 iterations. <br/>
<br/>
Bellow we can see how optimal actions change for each field during iterations.

<br/>
<img src="imgs/table_slip_02_discount_09.png"/>
<br/>

Here we can see what are the optimal actions after the algorithm has converged and what are the according V-values.
<br/>
<img src="imgs/block_slip_02_discount_09.png"/>

#### Slip probability=0.6
In this case agent goes to the target direction with probability of 0.4, but goes in orthogonal directions with probability 0.6 (0.3 each).
<br/>
The algorithm converges after 34 iterations. <br/>
<br/>
Here we can see what are the optimal actions after the algorithm has converged and what are the according V-values.
<br/>
<img src="imgs/block_slip_06_discount_09.png"/>


### Discount factor
Bellow we can see how the discount factor influences the performance. The analysis was performed with slip probability 0.2.
<br/>

#### Discount factor=0.9
The algorithm converges after 17 iterations.
<br/>
<img src="imgs/block_slip_02_discount_09.png"/>
<br/>

#### Discount factor=1.0
In this case the algorithm converges after 24 iterations. <br/>
Besides the V-values being higher than in the previous case (which was expected), we can notice some differences when it comes to optimal actions in the bottom row. This is because we are giving much more significance to the negative one-step-award: -0.04. 

<img src="imgs/block_slip_02_discount_10.png"/>
<br/>
