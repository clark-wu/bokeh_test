import {BokehEvent,ModelEvent} from "@bokehjs/core/bokeh_events"
import {Class} from "@bokehjs/core/class"

function event(event_name: string) {
    return function(cls: Class<BokehEvent>) {
      cls.prototype.event_name = event_name
    }
}

@event("move_up")
export class MoveUpEvent extends ModelEvent {}