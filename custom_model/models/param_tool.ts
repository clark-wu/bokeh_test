import {ActionTool, ActionToolView} from "@bokehjs/models/tools/actions/action_tool"
import * as p from "@bokehjs/core/properties"

export class ParamToolView extends ActionToolView {
  model: ParamTool

  doit(): void {
    window.prompt("x_range:",this.plot_view.model.x_range.toString())
  }
}

export namespace ParamTool {
  export type Attrs = p.AttrsOf<Props>

  export type Props = ActionTool.Props
}

export interface ParamTool extends ParamTool.Attrs {}

export class ParamTool extends ActionTool {
  properties: ParamTool.Props
  __view_type__: ParamToolView

  constructor(attrs?: Partial<ParamTool.Attrs>) {
    super(attrs)
  }
  static __module__ = "custom_model.models.param_tool"
  static init_ParamTool(): void {
    this.prototype.default_view = ParamToolView

    this.register_alias("param", () => new ParamTool())
  }

  tool_name = "Param"
}
