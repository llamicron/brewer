# Controller
## What it does
This is the main controller for the brew rig. It is responsible for switching valves and turning on the pump, RIMS, etc. It does this through [`str116`](str116.md) and [`omega`](omega.md)

## Constraints
This class (specifically classes that this class uses) depends on special hardware connected to a raspberry pi. This makes it a nightmare to develop, so I wrote a hardware simulator. When calling this class like you will below, it will *automagically* detect if there's hardware connected. If there's no hardware, it will return a class called `FakeController`. This will behave like the `Controller` class, but not use any hardware. The data it gives may not make much sense, because it's made up.

You can override this by setting the following environment variables:
```
$ export force_real_controller = 1
$ export force_fake_controller = 1
```
You probably won't want to do this, but idk.

## Properties
The `Controller` class currently has 3 main properties:
* `omega` - an instance of the `Omega` class. How the controller interfaces with the omega cn7500 PID
* `settings` - the settings module.
* `slack` - An instance of [`BrewerBot`](slack.md). Sends messages to the slack channel.


## Methods

```
@staticmethod
simulator()
```
returns an instance of `FakeController`


