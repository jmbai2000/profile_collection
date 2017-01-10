from ophyd import Device, Component as Cpt


class RGA(Device):
    startRGA = Cpt(EpicsSignal, 'Cmd:MID_Start-Cmd')
    stopRGA = Cpt(EpicsSignal, 'Cmd:ScanAbort-Cmd')
    mass1 = Cpt(EpicsSignalRO, 'P:MID1-I')
    mass2 = Cpt(EpicsSignalRO, 'P:MID2-I')
    mass3 = Cpt(EpicsSignalRO, 'P:MID3-I')
    mass4 = Cpt(EpicsSignalRO, 'P:MID4-I')

## We don't want the RGA to start and stop by any bluseky plan###
"""
    def stage(self):
        self.startRGA.put(1)

    def unstage(self):
        self.stopRGA.put(1)
                     

    def describe(self):
        res = super().describe()
        # This precision should be configured correctly in EPICS.
        for key in res:
            res[key]['precision'] = 10
        return res
 """

rga = RGA('XF:28IDA-VA{RGA:1}',
          name='rga',
          read_attrs=['mass1', 'mass2', 'mass3', 'mass4'])
