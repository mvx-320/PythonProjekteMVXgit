/****************************************************************************
**
** Copyright (C) 2021 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the examples of the Qt Design Studio.
**
** $QT_BEGIN_LICENSE:BSD$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** BSD License Usage
** Alternatively, you may use this file under the terms of the BSD license
** as follows:
**
** "Redistribution and use in source and binary forms, with or without
** modification, are permitted provided that the following conditions are
** met:
**   * Redistributions of source code must retain the above copyright
**     notice, this list of conditions and the following disclaimer.
**   * Redistributions in binary form must reproduce the above copyright
**     notice, this list of conditions and the following disclaimer in
**     the documentation and/or other materials provided with the
**     distribution.
**   * Neither the name of The Qt Company Ltd nor the names of its
**     contributors may be used to endorse or promote products derived
**     from this software without specific prior written permission.
**
**
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick 2.8
import QtQuick.Timeline 1.0

Item {
    id: smallbutton
    width: 43
    height: 43
    property alias lockedicononSource: lockediconon.source
    property alias currenticonoffSource: currenticonoff.source
    signal clicked

    MultSegmentArc {
        id: multiSegmentArc
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        maskColor: "#333333"
        timelineCurrentFrame: 0
        arcSegment1Source: "assets/smallArcSegment1.png"
        arcSegment2Source: "assets/smallArcSegment2.png"
        arcSegment3Source: "assets/smallArcSegment3.png"
        arcSegment4Source: "assets/smallArcSegment4.png"
    }

    Image {
        id: smallbuttoniconfill
        width: 39
        height: 39
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        source: "assets/smallbuttoniconfill.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: outllineoff
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        source: "assets/outllineoff.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: currenticonoff
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        source: "assets/currenticonoff.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: lockediconon
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        source: "assets/lockediconon.png"
        fillMode: Image.PreserveAspectFit
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
    }

    Connections {
        target: timelineAnimation
        onFinished: {
            clicked()
        }
    }

    Timeline {
        id: timeline
        animations: [
            TimelineAnimation {
                id: timelineAnimation
                loops: 1
                duration: 1000
                running: false
                to: 1000
                from: 0
                alwaysRunToEnd: false
            }
        ]
        enabled: false
        startFrame: 0
        endFrame: 1000

        KeyframeGroup {
            target: multiSegmentArc
            property: "timelineCurrentFrame"

            Keyframe {
                frame: 0
                value: 0
            }

            Keyframe {
                frame: 1000
                value: 1000
            }
        }
    }

    states: [
        State {
            name: "default"
            when: !mouseArea.pressed

            PropertyChanges {
                target: smallbuttoniconfill
                visible: false
            }

            PropertyChanges {
                target: lockediconon
                visible: false
            }

            PropertyChanges {
                target: timelineAnimation
                running: false
            }

            PropertyChanges {
                target: timeline
                enabled: false
            }

            PropertyChanges {
                target: outllineoff
                visible: true
            }

            PropertyChanges {
                target: currenticonoff
                visible: true
            }

            PropertyChanges {
                target: multiSegmentArc
                visible: false
            }
        },
        State {
            name: "pressed"
            when: mouseArea.pressed

            PropertyChanges {
                target: smallbuttoniconfill
                visible: true
            }

            PropertyChanges {
                target: lockediconon
                visible: true
            }

            PropertyChanges {
                target: timelineAnimation
                running: true
            }

            PropertyChanges {
                target: timeline
                enabled: true
            }

            PropertyChanges {
                target: outllineoff
                visible: false
            }

            PropertyChanges {
                target: currenticonoff
                visible: false
            }

            PropertyChanges {
                target: multiSegmentArc
                visible: true
            }
        },
        State {
            name: "complete"

            PropertyChanges {
                target: smallbuttoniconfill
                visible: true
            }

            PropertyChanges {
                target: lockediconon
                visible: true
            }

            PropertyChanges {
                target: timeline
                enabled: false
            }

            PropertyChanges {
                target: timelineAnimation
                running: false
            }

            PropertyChanges {
                target: outllineoff
                visible: true
            }

            PropertyChanges {
                target: currenticonoff
                visible: false
            }

            PropertyChanges {
                target: multiSegmentArc
                visible: true
            }
        }
    ]
}

