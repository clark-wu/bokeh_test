import {ActionTool, ActionToolView} from "@bokehjs/models/tools/actions/action_tool"
import * as p from "@bokehjs/core/properties"
import {MoveUpEvent} from "./bokeh_events"

export class MoveUpToolView extends ActionToolView {
  model: MoveUpTool

  doit(): void {
    this.plot_model.trigger_event(new MoveUpEvent())
  }
}

export namespace MoveUpTool {
  export type Attrs = p.AttrsOf<Props>

  export type Props = ActionTool.Props
}

export interface MoveUpTool extends MoveUpTool.Attrs {}

export class MoveUpTool extends ActionTool {
  properties: MoveUpTool.Props
  __view_type__: MoveUpToolView

  constructor(attrs?: Partial<MoveUpTool.Attrs>) {
    super(attrs)
  }
  static __module__ = "custom_model.models.move_up_tool"
  static init_MoveUpTool(): void {
    this.prototype.default_view = MoveUpToolView

    this.register_alias("moveup", () => new MoveUpTool())
  }

  tool_name = "MoveUp"
}
