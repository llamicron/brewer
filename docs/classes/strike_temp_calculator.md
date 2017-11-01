# Strike Temp Calculator
This module calculates the strike temp for the batch. Here's the only method:
```python
def calc_strike_temp(WaterVolInQuarts, GrainMassInPounds, GrainTemp, MashTemp):
    WaterToGrainRatio = WaterVolInQuarts / GrainMassInPounds
    StrikeWaterTemp = ((0.2 / WaterToGrainRatio) *
                       (MashTemp - GrainTemp)) + MashTemp
    return round(StrikeWaterTemp, 1)
```

It's pretty self explainatory, it's just some simple math. I am keeping it as a seperate module because I want to seperate what came directly from adaptiman/adaptibrew (`str116` is the other module). This is also the reason why this uses camelCase and not snake_case. I didn't write it.
