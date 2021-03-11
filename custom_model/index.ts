import * as custom_model from "./models"
export {custom_model}

import {register_models} from "@bokehjs/base"
register_models(custom_model as any)
