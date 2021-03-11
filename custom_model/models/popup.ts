import {Model} from "@bokehjs/model"
import {CustomAction} from "@bokehjs/models/tools/actions/custom_action"
import * as p from "@bokehjs/core/properties"

export namespace Popup {
  export type Attrs = p.AttrsOf<Props>

  export type Props = Model.Props & {
    message: p.Property<string>
  }
}

export interface Popup extends Popup.Attrs {}

export class Popup extends Model {
  properties: Popup.Props

  constructor(attrs?: Partial<Popup.Attrs>) {
    super(attrs)
  }
  static __module__ = "custom_model.models.popup"

  static init_Popup(): void {
    this.define<Popup.Props>({
      message: [ p.String, "" ]
    })
  }

  execute(action: CustomAction): void {
    
    window.alert(this.message.toString())
  }
}
