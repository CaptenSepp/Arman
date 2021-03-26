import unittest
from unittest.mock import MagicMock
from unittest.mock import call
import numpy as np
import matplotlib.pyplot as plt

from plotsinus import createPlot


class testPlotSinus(unittest.TestCase):
    def setUp(self):
        self.fig = plt.figure()

        self.expected_x = [0., 0.00502513, 0.01005025, 0.01507538, 0.0201005,
                  0.02512563, 0.03015075, 0.03517588, 0.04020101, 0.04522613,
                  0.05025126, 0.05527638, 0.06030151, 0.06532663, 0.07035176,
                  0.07537688, 0.08040201, 0.08542714, 0.09045226, 0.09547739,
                  0.10050251, 0.10552764, 0.11055276, 0.11557789, 0.12060302,
                  0.12562814, 0.13065327, 0.13567839, 0.14070352, 0.14572864,
                  0.15075377, 0.15577889, 0.16080402, 0.16582915, 0.17085427,
                  0.1758794, 0.18090452, 0.18592965, 0.19095477, 0.1959799,
                  0.20100503, 0.20603015, 0.21105528, 0.2160804, 0.22110553,
                  0.22613065, 0.23115578, 0.2361809, 0.24120603, 0.24623116,
                  0.25125628, 0.25628141, 0.26130653, 0.26633166, 0.27135678,
                  0.27638191, 0.28140704, 0.28643216, 0.29145729, 0.29648241,
                  0.30150754, 0.30653266, 0.31155779, 0.31658291, 0.32160804,
                  0.32663317, 0.33165829, 0.33668342, 0.34170854, 0.34673367,
                  0.35175879, 0.35678392, 0.36180905, 0.36683417, 0.3718593,
                  0.37688442, 0.38190955, 0.38693467, 0.3919598, 0.39698492,
                  0.40201005, 0.40703518, 0.4120603, 0.41708543, 0.42211055,
                  0.42713568, 0.4321608, 0.43718593, 0.44221106, 0.44723618,
                  0.45226131, 0.45728643, 0.46231156, 0.46733668, 0.47236181,
                  0.47738693, 0.48241206, 0.48743719, 0.49246231, 0.49748744,
                  0.50251256, 0.50753769, 0.51256281, 0.51758794, 0.52261307,
                  0.52763819, 0.53266332, 0.53768844, 0.54271357, 0.54773869,
                  0.55276382, 0.55778894, 0.56281407, 0.5678392, 0.57286432,
                  0.57788945, 0.58291457, 0.5879397, 0.59296482, 0.59798995,
                  0.60301508, 0.6080402, 0.61306533, 0.61809045, 0.62311558,
                  0.6281407, 0.63316583, 0.63819095, 0.64321608, 0.64824121,
                  0.65326633, 0.65829146, 0.66331658, 0.66834171, 0.67336683,
                  0.67839196, 0.68341709, 0.68844221, 0.69346734, 0.69849246,
                  0.70351759, 0.70854271, 0.71356784, 0.71859296, 0.72361809,
                  0.72864322, 0.73366834, 0.73869347, 0.74371859, 0.74874372,
                  0.75376884, 0.75879397, 0.7638191, 0.76884422, 0.77386935,
                  0.77889447, 0.7839196, 0.78894472, 0.79396985, 0.79899497,
                  0.8040201, 0.80904523, 0.81407035, 0.81909548, 0.8241206,
                  0.82914573, 0.83417085, 0.83919598, 0.84422111, 0.84924623,
                  0.85427136, 0.85929648, 0.86432161, 0.86934673, 0.87437186,
                  0.87939698, 0.88442211, 0.88944724, 0.89447236, 0.89949749,
                  0.90452261, 0.90954774, 0.91457286, 0.91959799, 0.92462312,
                  0.92964824, 0.93467337, 0.93969849, 0.94472362, 0.94974874,
                  0.95477387, 0.95979899, 0.96482412, 0.96984925, 0.97487437,
                  0.9798995, 0.98492462, 0.98994975, 0.99497487, 1.]
        self.expected_y1 = [ 0.        ,  0.04147184,  0.08265788,  0.12327428,  0.16304113,
        0.20168437,  0.23893771,  0.2745444 ,  0.30825905,  0.33984933,
        0.36909754,  0.39580209,  0.41977896,  0.44086292,  0.45890866,
        0.47379181,  0.48540982,  0.49368261,  0.49855317,  0.49998794,
        0.49797703,  0.49253429,  0.48369725,  0.47152678,  0.45610678,
        0.43754351,  0.4159649 ,  0.39151965,  0.36437623,  0.3347217 ,
        0.30276043,  0.26871268,  0.23281308,  0.19530905,  0.15645904,
        0.11653079,  0.07579946,  0.03454576, -0.00694601, -0.04838992,
       -0.08950034, -0.12999397, -0.16959174, -0.20802077, -0.24501622,
       -0.28032313, -0.31369818, -0.34491138, -0.37374761, -0.40000815,
       -0.42351202, -0.44409724, -0.46162196, -0.4759654 , -0.4870287 ,
       -0.49473564, -0.49903309, -0.49989144, -0.49730478, -0.49129092,
       -0.48189132, -0.46917076, -0.45321689, -0.43413966, -0.41207055,
       -0.38716164, -0.35958459, -0.32952946, -0.29720337, -0.26282909,
       -0.22664352, -0.18889603, -0.14984676, -0.10976481, -0.06892642,
       -0.02761302,  0.01389068,  0.05529865,  0.09632553,  0.13668858,
        0.17610963,  0.21431702,  0.25104744,  0.28604776,  0.31907677,
        0.34990686,  0.37832555,  0.404137  ,  0.42716333,  0.44724586,
        0.46424617,  0.47804712,  0.4885536 ,  0.49569319,  0.4994167 ,
        0.49969847,  0.49653655,  0.48995273,  0.4799924 ,  0.46672418,
        0.45023952,  0.43065202,  0.40809667,  0.38272891,  0.35472356,
        0.32427363,  0.29158896,  0.25689479,  0.22043022,  0.18244656,
        0.14320556,  0.10297765,  0.06204007,  0.02067494, -0.02083267,
       -0.06219672, -0.10313213, -0.1433568 , -0.18259353, -0.22057191,
       -0.25703021, -0.29171719, -0.32439378, -0.3548348 , -0.38283048,
       -0.40818786, -0.43073221, -0.45030815, -0.46678078, -0.48003658,
       -0.4899842 , -0.49655507, -0.49970392, -0.49940905, -0.49567249,
       -0.48851998, -0.47800083, -0.46418752, -0.44717525, -0.42708126,
       -0.40404403, -0.37822231, -0.34979407, -0.31895521, -0.28591826,
       -0.2509109 , -0.21417438, -0.17596187, -0.13653672, -0.09617061,
       -0.05514175, -0.01373287,  0.02777064,  0.06908278,  0.10991882,
        0.14999736,  0.18904219,  0.22678423,  0.26296338,  0.29733031,
        0.32964818,  0.35969427,  0.38726152,  0.41215994,  0.43421795,
        0.45328354,  0.46922531,  0.4819334 ,  0.49132023,  0.49732112,
        0.49989471,  0.49902325,  0.49471277,  0.48699295,  0.47591701,
        0.46156128,  0.44402468,  0.42342808,  0.39991341,  0.37364272,
        0.34479707,  0.31357524,  0.28019239,  0.24487859,  0.2078772 ,
        0.16944323,  0.12984152,  0.08934502,  0.04823279,  0.00678816,
       -0.03470325, -0.0759555 , -0.1166843 , -0.15660897, -0.19545437,
       -0.23295278, -0.26884579, -0.30288605, -0.33483896, -0.36448431]

        self.expected_y2 = [-0.28678822, -0.25182827, -0.21513284, -0.17695482, -0.1375573 ,
       -0.09721181, -0.05619638, -0.01479367,  0.02671099,  0.06803157,
        0.10888331,  0.14898468,  0.18805931,  0.22583793,  0.26206018,
        0.29647644,  0.32884952,  0.35895632,  0.38658937,  0.41155822,
        0.43369081,  0.45283461,  0.46885769,  0.48164962,  0.49112225,
        0.49721029,  0.4998718 ,  0.49908843,  0.49486557,  0.48723234,
        0.47624133,  0.46196829,  0.44451158,  0.42399151,  0.40054949,
        0.37434707,  0.34556483,  0.31440112,  0.2810707 ,  0.24580328,
        0.2088419 ,  0.17044128,  0.13086606,  0.09038897,  0.04928896,
        0.00784927, -0.0336445 , -0.07490642, -0.11565211, -0.15560079,
       -0.19447714, -0.23201324, -0.26795042, -0.30204101, -0.33405008,
       -0.36375703, -0.39095714, -0.41546296, -0.4371056 , -0.45573592,
       -0.47122552, -0.48346766, -0.49237796, -0.49789503, -0.49998085,
       -0.49862103, -0.49382495, -0.48562566, -0.47407967, -0.45926654,
       -0.44128837, -0.42026905, -0.39635343, -0.36970633, -0.34051139,
       -0.3089698 , -0.27529894, -0.23973085, -0.20251065, -0.16389484,
       -0.12414955, -0.08354867, -0.04237202, -0.00090336,  0.04057153,
        0.08176681,  0.1223986 ,  0.16218688,  0.20085743,  0.23814378,
        0.27378895,  0.3075473 ,  0.33918617,  0.36848754,  0.39524946,
        0.41928751,  0.44043603,  0.45854927,  0.47350241,  0.48519239,
        0.49353865,  0.49848368,  0.4999934 ,  0.49805739,  0.49268901,
        0.48392525,  0.47182651,  0.45647616,  0.43797999,  0.41646547,
        0.39208087,  0.36499423,  0.33539223,  0.30347886,  0.26947405,
        0.23361216,  0.19614032,  0.15731678,  0.11740908,  0.07669226,
        0.03544691, -0.00604273, -0.04749072, -0.08861142, -0.12912146,
       -0.16874166, -0.20719897, -0.24422835, -0.27957464, -0.31299422,
       -0.3442568 , -0.37314693, -0.3994655 , -0.42303114, -0.44368145,
       -0.46127412, -0.47568791, -0.48682348, -0.49460409, -0.49897612,
       -0.49990945, -0.49739764, -0.49145799, -0.48213145, -0.46948229,
       -0.45359768, -0.43458708, -0.41258152, -0.38773264, -0.36021169,
       -0.33020834, -0.29792934, -0.26359715, -0.22744838, -0.18973214,
       -0.15070835, -0.11064596, -0.06982104, -0.02851495,  0.01298765,
        0.05440074,  0.09543893,  0.13581941,  0.17526387,  0.21350051,
        0.25026579,  0.28530637,  0.31838075,  0.34926099,  0.3777343 ,
        0.40360444,  0.42669313,  0.44684125,  0.46390995,  0.4777816 ,
        0.48836061,  0.49557407,  0.49937226,  0.49972902,  0.49664188,
        0.49013212,  0.4802446 ,  0.46704746,  0.45063165,  0.4311103 ,
        0.40861794,  0.38330958,  0.35535964,  0.32496072,  0.29232232,
        0.25766938,  0.2212407 ,  0.18328733,  0.14407084,  0.10386148,
        0.06293635,  0.02157749, -0.01993006, -0.06130027, -0.10224803]

    def testLabels(self):
        ax = self.fig.gca()
        createPlot(ax)
        self.assertEqual(len(ax.lines), 2)
        self.assertEqual(ax.lines[0].get_label(), '2.63 MHz mit 0° Phasenverschiebung')
        self.assertEqual(ax.lines[1].get_label(), '2.63 MHz mit 35° Phasenverschiebung')

    def testLinestyle(self):
        ax = self.fig.gca()
        createPlot(ax)
        self.assertEqual(len(ax.lines), 2)
        self.assertEqual(ax.lines[0].get_linestyle(), '-')
        self.assertEqual(ax.lines[1].get_linestyle(), '--')

    def testAxisLabels(self):
        ax = self.fig.gca()
        createPlot(ax)

        self.assertEqual(ax.get_ylabel(), "Amplitude in mV")
        self.assertEqual(ax.get_xlabel(), "Zeit in us")

    def testTitle(self):
        ax = self.fig.gca()
        createPlot(ax)
        self.assertEqual("Zwei versetzte Sinussignale", ax.title._text)

    def testYLim(self):
        ax = self.fig.gca()
        createPlot(ax)
        self.assertEqual(ax.get_ylim(), (-1.5, 2.0))

    def testLegendLocation(self):
        ax = self.fig.gca()
        createPlot(ax)
        self.assertIsNotNone(ax.get_legend())
        self.assertEqual(ax.get_legend()._get_loc(), 2)

    def testGrid(self):
        ax = MagicMock()
        createPlot(ax)
        ax.grid.assert_called()

    def testColor(self):
        ax = self.fig.gca()
        createPlot(ax)

        self.assertEqual(len(ax.lines), 2)
        self.assertTrue(ax.lines[0].get_color() in  ['black', 'k'])
        self.assertTrue(ax.lines[1].get_color() in  ['black', 'k'])



    def testXValues(self):
        ax = self.fig.gca()
        createPlot(ax)

        self.assertEqual(len(ax.lines), 2)
        x = ax.lines[0]._x
        np.testing.assert_array_almost_equal(x, self.expected_x)

    def testYValues(self):
        ax = self.fig.gca()
        createPlot(ax)

        self.assertEqual(len(ax.lines), 2)
        y1 = ax.lines[0]._y
        np.testing.assert_array_almost_equal(y1, self.expected_y1)
        y2 = ax.lines[1]._y
        np.testing.assert_array_almost_equal(y2, self.expected_y2)
