<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `buildcraft.robotics.ai.AIRobotSearchStackRequest#getOrderFromRequestingStation(DockingStation,boolean)`\
target: `buildcraft.robotics.ai.AIRobotSearchStackRequest#getAvailableRequests(DockingStation)`\
type: `EXTRACT`\
commit: [a5cdd8c4b](https://github.com/BuildCraft/BuildCraft/commit/a5cdd8c4b10a738cb44819d7cc2fee5f5965d4a0)\
description: `Extract Method private getAvailableRequests(station DockingStation) : Collection<StackRequest> extracted from private getOrderFromRequestingStation(station DockingStation, take boolean) : StackRequest in class buildcraft.robotics.ai.AIRobotSearchStackRequest`

id: `1`\
source `buildcraft.robotics.ai.AIRobotSearchStackRequest#getOrderFromRequestingStation(DockingStation,boolean)`\
target: `buildcraft.robotics.StackRequest#setStation(DockingStation)`\
type: `EXTRACT_MOVE`\
commit: [a5cdd8c4b](https://github.com/BuildCraft/BuildCraft/commit/a5cdd8c4b10a738cb44819d7cc2fee5f5965d4a0)\
description: `Extract And Move Method public setStation(station DockingStation) : void extracted from private getOrderFromRequestingStation(station DockingStation, take boolean) : StackRequest in class buildcraft.robotics.ai.AIRobotSearchStackRequest & moved to class buildcraft.robotics.StackRequest`

