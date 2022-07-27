import QtQuick 6.2
import QtQuick.Controls 6.2
import QtObject.Controls 1.4 as Cl

ApplicationWindow{
    id: window
    width: 600
    height: 400
    visible: true
    color: "white"
    title: qsTr("test page")
    Cl.TabView {
        Cl.Tab {
            title: "Red"
            Rectangle {
                color: "red"
            }
        }
        Cl.Tab {
            title: "Blue"
            Rectangle {
                color: "blue"
            }
        }
        Cl.Tab {
            title: "Green"
            Rectangle {
                color: "green"
            }
        }
    }
}