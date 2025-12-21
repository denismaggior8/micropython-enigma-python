from assertion import assert_eq, assert_true, assert_false
from base_test import BaseTest
from enigmapython.SwappablePlugboard import SwappablePlugboard

class SwappablePlugboardTestCase(BaseTest):

    def test_swappable_plugboard_init_method(self):
        plugboard = SwappablePlugboard({"a":"z","b":"c"})
        return assert_eq(plugboard.wiring,"zcbdefghijklmnopqrstuvwxya", "Plugboard swap failed")
    
def run():
    return SwappablePlugboardTestCase().run()

if __name__ == "__main__":
    run()