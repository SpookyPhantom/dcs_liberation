from PySide2.QtWidgets import QGraphicsRectItem

import qt_ui.uiconstants as CONST
from theater import TheaterGroundObject, ControlPoint


class QMapGroundObject(QGraphicsRectItem):

    def __init__(self, parent, x: float, y: float, w: float, h: float, cp: ControlPoint, model: TheaterGroundObject):
        super(QMapGroundObject, self).__init__(x, y, w, h)
        self.model = model
        self.cp = cp
        self.parent = parent
        self.setAcceptHoverEvents(True)
        self.setZValue(2)
        self.setToolTip(cp.name + "'s " + self.model.category)


    def paint(self, painter, option, widget=None):
        #super(QMapControlPoint, self).paint(painter, option, widget)

        if self.parent.get_display_rule("go"):
            painter.save()
            if not self.model.is_dead and not self.cp.captured:
                painter.drawPixmap(option.rect, CONST.ICONS[self.model.category])
            else:
                painter.drawPixmap(option.rect, CONST.ICONS["cleared"])
            painter.restore()
