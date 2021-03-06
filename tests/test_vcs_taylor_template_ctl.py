import basevcstest
import MV2

class TestVCSTaylor(basevcstest.VCSBaseTest):
    def testVCSTaylor(self):

        ## Create a template from the default taylor diagram
        t=self.x.createtemplate('mytaylor','deftaylor')

        ## Create a taylordiagrma graphic method
        td=self.x.createtaylordiagram('my')

        self.x.portrait()

        ## Create a line which we will make dotted and grey
        gdl=self.x.createline('gdl')
        gdl.color=["grey",]
        gdl.type='dot'
        ## Create a line which we will make grey
        gl=self.x.createline('gl')
        gl.color=["grey",]
        gl.type='solid'


        # Now make the template grid appear and extend thru
        # the whole grid
        t.ytic2.x1=t.data.x1
        t.ytic2.x2=t.data.x2
        t.ytic2.line='gl'

        ## Same for the min tics
        t.ymintic2.x1=t.data.x1
        t.ymintic2.x2=t.data.x2
        t.ymintic2.line='gdl'

        # Same thing the circles
        t.xtic2.y1=t.data.y1
        t.xtic2.y2=t.data.y2
        t.xtic2.line='gl'
        # Same thing the mintic circles
        t.xmintic2.y1=t.data.y1
        t.xmintic2.y2=t.data.y2
        t.xmintic2.line='gdl'

        # turn the circles on
        t.xtic2.priority=1
        t.xmintic2.priority=1

        # Create some dummy data for display purposes
        data=MV2.array([[1.52,.52,],[.83,.84]])

        self.x.plot(data, t, td, bg=self.bg)
        self.checkImage("test_vcs_taylor_template_ctl.png")
