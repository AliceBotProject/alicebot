# alicebot.adapter.telegram.model

Telegram 模型。

## _class_ `Response` {#Response}

Bases: `pydantic.main.BaseModel`, `typing.Generic`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **ok** (_bool_)

  - **description** (_Optional\[str\]_)

  - **result** (_Optional\[~\_T\]_)

  - **error\_code** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `User` {#User}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **id** (_int_)

  - **is\_bot** (_bool_)

  - **first\_name** (_str_)

  - **last\_name** (_Optional\[str\]_)

  - **username** (_Optional\[str\]_)

  - **language\_code** (_Optional\[str\]_)

  - **is\_premium** (_Optional\[bool\]_)

  - **added\_to\_attachment\_menu** (_Optional\[bool\]_)

  - **can\_join\_groups** (_Optional\[bool\]_)

  - **can\_read\_all\_group\_messages** (_Optional\[bool\]_)

  - **supports\_inline\_queries** (_Optional\[bool\]_)

  - **can\_connect\_to\_business** (_Optional\[bool\]_)

  - **has\_main\_web\_app** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Chat` {#Chat}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **id** (_int_)

  - **type** (_str_)

  - **title** (_Optional\[str\]_)

  - **username** (_Optional\[str\]_)

  - **first\_name** (_Optional\[str\]_)

  - **last\_name** (_Optional\[str\]_)

  - **is\_forum** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MessageOriginUser` {#MessageOriginUser}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **date** (_int_)

  - **sender\_user** (_User_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MessageOriginHiddenUser` {#MessageOriginHiddenUser}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **date** (_int_)

  - **sender\_user\_name** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MessageOriginChat` {#MessageOriginChat}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **date** (_int_)

  - **sender\_chat** (_Chat_)

  - **author\_signature** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MessageOriginChannel` {#MessageOriginChannel}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **date** (_int_)

  - **chat** (_Chat_)

  - **message\_id** (_int_)

  - **author\_signature** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `LinkPreviewOptions` {#LinkPreviewOptions}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **is\_disabled** (_Optional\[bool\]_)

  - **url** (_Optional\[str\]_)

  - **prefer\_small\_media** (_Optional\[bool\]_)

  - **prefer\_large\_media** (_Optional\[bool\]_)

  - **show\_above\_text** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PhotoSize` {#PhotoSize}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **file\_id** (_str_)

  - **file\_unique\_id** (_str_)

  - **width** (_int_)

  - **height** (_int_)

  - **file\_size** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Animation` {#Animation}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **file\_id** (_str_)

  - **file\_unique\_id** (_str_)

  - **width** (_int_)

  - **height** (_int_)

  - **duration** (_int_)

  - **thumbnail** (_Optional\[alicebot.adapter.telegram.model.PhotoSize\]_)

  - **file\_name** (_Optional\[str\]_)

  - **mime\_type** (_Optional\[str\]_)

  - **file\_size** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Audio` {#Audio}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **file\_id** (_str_)

  - **file\_unique\_id** (_str_)

  - **duration** (_int_)

  - **performer** (_Optional\[str\]_)

  - **title** (_Optional\[str\]_)

  - **file\_name** (_Optional\[str\]_)

  - **mime\_type** (_Optional\[str\]_)

  - **file\_size** (_Optional\[int\]_)

  - **thumbnail** (_Optional\[alicebot.adapter.telegram.model.PhotoSize\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Document` {#Document}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **file\_id** (_str_)

  - **file\_unique\_id** (_str_)

  - **thumbnail** (_Optional\[alicebot.adapter.telegram.model.PhotoSize\]_)

  - **file\_name** (_Optional\[str\]_)

  - **mime\_type** (_Optional\[str\]_)

  - **file\_size** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PaidMediaPreview` {#PaidMediaPreview}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **width** (_Optional\[int\]_)

  - **height** (_Optional\[int\]_)

  - **duration** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PaidMediaPhoto` {#PaidMediaPhoto}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **photo** (_list\[alicebot.adapter.telegram.model.PhotoSize\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Video` {#Video}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **file\_id** (_str_)

  - **file\_unique\_id** (_str_)

  - **width** (_int_)

  - **height** (_int_)

  - **duration** (_int_)

  - **thumbnail** (_Optional\[alicebot.adapter.telegram.model.PhotoSize\]_)

  - **file\_name** (_Optional\[str\]_)

  - **mime\_type** (_Optional\[str\]_)

  - **file\_size** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PaidMediaVideo` {#PaidMediaVideo}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **video** (_Video_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PaidMediaInfo` {#PaidMediaInfo}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **star\_count** (_int_)

  - **paid\_media** (_list\[typing.Union\[alicebot.adapter.telegram.model.PaidMediaPreview, alicebot.adapter.telegram.model.PaidMediaPhoto, alicebot.adapter.telegram.model.PaidMediaVideo\]\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `File` {#File}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **file\_id** (_str_)

  - **file\_unique\_id** (_str_)

  - **file\_size** (_Optional\[int\]_)

  - **file\_path** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MaskPosition` {#MaskPosition}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **point** (_str_)

  - **x\_shift** (_float_)

  - **y\_shift** (_float_)

  - **scale** (_float_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Sticker` {#Sticker}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **file\_id** (_str_)

  - **file\_unique\_id** (_str_)

  - **type** (_str_)

  - **width** (_int_)

  - **height** (_int_)

  - **is\_animated** (_bool_)

  - **is\_video** (_bool_)

  - **thumbnail** (_Optional\[alicebot.adapter.telegram.model.PhotoSize\]_)

  - **emoji** (_Optional\[str\]_)

  - **set\_name** (_Optional\[str\]_)

  - **premium\_animation** (_Optional\[alicebot.adapter.telegram.model.File\]_)

  - **mask\_position** (_Optional\[alicebot.adapter.telegram.model.MaskPosition\]_)

  - **custom\_emoji\_id** (_Optional\[str\]_)

  - **needs\_repainting** (_Optional\[bool\]_)

  - **file\_size** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Story` {#Story}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **chat** (_Chat_)

  - **id** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `VideoNote` {#VideoNote}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **file\_id** (_str_)

  - **file\_unique\_id** (_str_)

  - **length** (_int_)

  - **duration** (_int_)

  - **thumbnail** (_Optional\[alicebot.adapter.telegram.model.PhotoSize\]_)

  - **file\_size** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Voice` {#Voice}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **file\_id** (_str_)

  - **file\_unique\_id** (_str_)

  - **duration** (_int_)

  - **mime\_type** (_Optional\[str\]_)

  - **file\_size** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Contact` {#Contact}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **phone\_number** (_str_)

  - **first\_name** (_str_)

  - **last\_name** (_Optional\[str\]_)

  - **user\_id** (_Optional\[int\]_)

  - **vcard** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Dice` {#Dice}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **emoji** (_str_)

  - **value** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MessageEntity` {#MessageEntity}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **offset** (_int_)

  - **length** (_int_)

  - **url** (_Optional\[str\]_)

  - **user** (_Optional\[alicebot.adapter.telegram.model.User\]_)

  - **language** (_Optional\[str\]_)

  - **custom\_emoji\_id** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Game` {#Game}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **title** (_str_)

  - **description** (_str_)

  - **photo** (_list\[alicebot.adapter.telegram.model.PhotoSize\]_)

  - **text** (_Optional\[str\]_)

  - **text\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **animation** (_Optional\[alicebot.adapter.telegram.model.Animation\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Giveaway` {#Giveaway}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **chats** (_list\[alicebot.adapter.telegram.model.Chat\]_)

  - **winners\_selection\_date** (_int_)

  - **winner\_count** (_int_)

  - **only\_new\_members** (_Optional\[bool\]_)

  - **has\_public\_winners** (_Optional\[bool\]_)

  - **prize\_description** (_Optional\[str\]_)

  - **country\_codes** (_Optional\[list\[str\]\]_)

  - **prize\_star\_count** (_Optional\[int\]_)

  - **premium\_subscription\_month\_count** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `GiveawayWinners` {#GiveawayWinners}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **chat** (_Chat_)

  - **giveaway\_message\_id** (_int_)

  - **winners\_selection\_date** (_int_)

  - **winner\_count** (_int_)

  - **winners** (_list\[alicebot.adapter.telegram.model.User\]_)

  - **additional\_chat\_count** (_Optional\[int\]_)

  - **prize\_star\_count** (_Optional\[int\]_)

  - **premium\_subscription\_month\_count** (_Optional\[int\]_)

  - **unclaimed\_prize\_count** (_Optional\[int\]_)

  - **only\_new\_members** (_Optional\[bool\]_)

  - **was\_refunded** (_Optional\[bool\]_)

  - **prize\_description** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Invoice` {#Invoice}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **title** (_str_)

  - **description** (_str_)

  - **start\_parameter** (_str_)

  - **currency** (_str_)

  - **total\_amount** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Location` {#Location}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **latitude** (_float_)

  - **longitude** (_float_)

  - **horizontal\_accuracy** (_Optional\[float\]_)

  - **live\_period** (_Optional\[int\]_)

  - **heading** (_Optional\[int\]_)

  - **proximity\_alert\_radius** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PollOption` {#PollOption}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **text** (_str_)

  - **text\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **voter\_count** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Poll` {#Poll}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **id** (_str_)

  - **question** (_str_)

  - **question\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **options** (_list\[alicebot.adapter.telegram.model.PollOption\]_)

  - **total\_voter\_count** (_int_)

  - **is\_closed** (_bool_)

  - **is\_anonymous** (_bool_)

  - **type** (_str_)

  - **allows\_multiple\_answers** (_bool_)

  - **correct\_option\_id** (_Optional\[int\]_)

  - **explanation** (_Optional\[str\]_)

  - **explanation\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **open\_period** (_Optional\[int\]_)

  - **close\_date** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Venue` {#Venue}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **location** (_Location_)

  - **title** (_str_)

  - **address** (_str_)

  - **foursquare\_id** (_Optional\[str\]_)

  - **foursquare\_type** (_Optional\[str\]_)

  - **google\_place\_id** (_Optional\[str\]_)

  - **google\_place\_type** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ExternalReplyInfo` {#ExternalReplyInfo}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **origin** (_Union\[alicebot.adapter.telegram.model.MessageOriginUser, alicebot.adapter.telegram.model.MessageOriginHiddenUser, alicebot.adapter.telegram.model.MessageOriginChat, alicebot.adapter.telegram.model.MessageOriginChannel\]_)

  - **chat** (_Optional\[alicebot.adapter.telegram.model.Chat\]_)

  - **message\_id** (_Optional\[int\]_)

  - **link\_preview\_options** (_Optional\[alicebot.adapter.telegram.model.LinkPreviewOptions\]_)

  - **animation** (_Optional\[alicebot.adapter.telegram.model.Animation\]_)

  - **audio** (_Optional\[alicebot.adapter.telegram.model.Audio\]_)

  - **document** (_Optional\[alicebot.adapter.telegram.model.Document\]_)

  - **paid\_media** (_Optional\[alicebot.adapter.telegram.model.PaidMediaInfo\]_)

  - **photo** (_Optional\[list\[alicebot.adapter.telegram.model.PhotoSize\]\]_)

  - **sticker** (_Optional\[alicebot.adapter.telegram.model.Sticker\]_)

  - **story** (_Optional\[alicebot.adapter.telegram.model.Story\]_)

  - **video** (_Optional\[alicebot.adapter.telegram.model.Video\]_)

  - **video\_note** (_Optional\[alicebot.adapter.telegram.model.VideoNote\]_)

  - **voice** (_Optional\[alicebot.adapter.telegram.model.Voice\]_)

  - **has\_media\_spoiler** (_Optional\[bool\]_)

  - **contact** (_Optional\[alicebot.adapter.telegram.model.Contact\]_)

  - **dice** (_Optional\[alicebot.adapter.telegram.model.Dice\]_)

  - **game** (_Optional\[alicebot.adapter.telegram.model.Game\]_)

  - **giveaway** (_Optional\[alicebot.adapter.telegram.model.Giveaway\]_)

  - **giveaway\_winners** (_Optional\[alicebot.adapter.telegram.model.GiveawayWinners\]_)

  - **invoice** (_Optional\[alicebot.adapter.telegram.model.Invoice\]_)

  - **location** (_Optional\[alicebot.adapter.telegram.model.Location\]_)

  - **poll** (_Optional\[alicebot.adapter.telegram.model.Poll\]_)

  - **venue** (_Optional\[alicebot.adapter.telegram.model.Venue\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `TextQuote` {#TextQuote}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **text** (_str_)

  - **entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **position** (_int_)

  - **is\_manual** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MessageAutoDeleteTimerChanged` {#MessageAutoDeleteTimerChanged}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **message\_auto\_delete\_time** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InaccessibleMessage` {#InaccessibleMessage}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **chat** (_Chat_)

  - **message\_id** (_int_)

  - **date** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ShippingAddress` {#ShippingAddress}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **country\_code** (_str_)

  - **state** (_str_)

  - **city** (_str_)

  - **street\_line1** (_str_)

  - **street\_line2** (_str_)

  - **post\_code** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `OrderInfo` {#OrderInfo}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **name** (_Optional\[str\]_)

  - **phone\_number** (_Optional\[str\]_)

  - **email** (_Optional\[str\]_)

  - **shipping\_address** (_Optional\[alicebot.adapter.telegram.model.ShippingAddress\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `SuccessfulPayment` {#SuccessfulPayment}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **currency** (_str_)

  - **total\_amount** (_int_)

  - **invoice\_payload** (_str_)

  - **shipping\_option\_id** (_Optional\[str\]_)

  - **order\_info** (_Optional\[alicebot.adapter.telegram.model.OrderInfo\]_)

  - **telegram\_payment\_charge\_id** (_str_)

  - **provider\_payment\_charge\_id** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `RefundedPayment` {#RefundedPayment}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **currency** (_str_)

  - **total\_amount** (_int_)

  - **invoice\_payload** (_str_)

  - **telegram\_payment\_charge\_id** (_str_)

  - **provider\_payment\_charge\_id** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `SharedUser` {#SharedUser}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **user\_id** (_int_)

  - **first\_name** (_Optional\[str\]_)

  - **last\_name** (_Optional\[str\]_)

  - **username** (_Optional\[str\]_)

  - **photo** (_Optional\[list\[alicebot.adapter.telegram.model.PhotoSize\]\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `UsersShared` {#UsersShared}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **request\_id** (_int_)

  - **users** (_list\[alicebot.adapter.telegram.model.SharedUser\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatShared` {#ChatShared}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **request\_id** (_int_)

  - **chat\_id** (_int_)

  - **title** (_Optional\[str\]_)

  - **username** (_Optional\[str\]_)

  - **photo** (_Optional\[list\[alicebot.adapter.telegram.model.PhotoSize\]\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `WriteAccessAllowed` {#WriteAccessAllowed}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **from\_request** (_Optional\[bool\]_)

  - **web\_app\_name** (_Optional\[str\]_)

  - **from\_attachment\_menu** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PassportFile` {#PassportFile}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **file\_id** (_str_)

  - **file\_unique\_id** (_str_)

  - **file\_size** (_int_)

  - **file\_date** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `EncryptedPassportElement` {#EncryptedPassportElement}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **data** (_Optional\[str\]_)

  - **phone\_number** (_Optional\[str\]_)

  - **email** (_Optional\[str\]_)

  - **files** (_Optional\[list\[alicebot.adapter.telegram.model.PassportFile\]\]_)

  - **front\_side** (_Optional\[alicebot.adapter.telegram.model.PassportFile\]_)

  - **reverse\_side** (_Optional\[alicebot.adapter.telegram.model.PassportFile\]_)

  - **selfie** (_Optional\[alicebot.adapter.telegram.model.PassportFile\]_)

  - **translation** (_Optional\[list\[alicebot.adapter.telegram.model.PassportFile\]\]_)

  - **hash** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `EncryptedCredentials` {#EncryptedCredentials}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **data** (_str_)

  - **hash** (_str_)

  - **secret** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PassportData` {#PassportData}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **data** (_list\[alicebot.adapter.telegram.model.EncryptedPassportElement\]_)

  - **credentials** (_EncryptedCredentials_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ProximityAlertTriggered` {#ProximityAlertTriggered}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **traveler** (_User_)

  - **watcher** (_User_)

  - **distance** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatBoostAdded` {#ChatBoostAdded}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **boost\_count** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BackgroundFillSolid` {#BackgroundFillSolid}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **color** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BackgroundFillGradient` {#BackgroundFillGradient}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **top\_color** (_int_)

  - **bottom\_color** (_int_)

  - **rotation\_angle** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BackgroundFillFreeformGradient` {#BackgroundFillFreeformGradient}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **colors** (_list\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BackgroundTypeFill` {#BackgroundTypeFill}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **fill** (_Union\[alicebot.adapter.telegram.model.BackgroundFillSolid, alicebot.adapter.telegram.model.BackgroundFillGradient, alicebot.adapter.telegram.model.BackgroundFillFreeformGradient\]_)

  - **dark\_theme\_dimming** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BackgroundTypeWallpaper` {#BackgroundTypeWallpaper}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **document** (_Document_)

  - **dark\_theme\_dimming** (_int_)

  - **is\_blurred** (_Optional\[bool\]_)

  - **is\_moving** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BackgroundTypePattern` {#BackgroundTypePattern}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **document** (_Document_)

  - **fill** (_Union\[alicebot.adapter.telegram.model.BackgroundFillSolid, alicebot.adapter.telegram.model.BackgroundFillGradient, alicebot.adapter.telegram.model.BackgroundFillFreeformGradient\]_)

  - **intensity** (_int_)

  - **is\_inverted** (_Optional\[bool\]_)

  - **is\_moving** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BackgroundTypeChatTheme` {#BackgroundTypeChatTheme}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **theme\_name** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatBackground` {#ChatBackground}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_Union\[alicebot.adapter.telegram.model.BackgroundTypeFill, alicebot.adapter.telegram.model.BackgroundTypeWallpaper, alicebot.adapter.telegram.model.BackgroundTypePattern, alicebot.adapter.telegram.model.BackgroundTypeChatTheme\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ForumTopicCreated` {#ForumTopicCreated}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **name** (_str_)

  - **icon\_color** (_int_)

  - **icon\_custom\_emoji\_id** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ForumTopicEdited` {#ForumTopicEdited}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **name** (_Optional\[str\]_)

  - **icon\_custom\_emoji\_id** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ForumTopicClosed` {#ForumTopicClosed}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ForumTopicReopened` {#ForumTopicReopened}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `GeneralForumTopicHidden` {#GeneralForumTopicHidden}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `GeneralForumTopicUnhidden` {#GeneralForumTopicUnhidden}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `GiveawayCreated` {#GiveawayCreated}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **prize\_star\_count** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `GiveawayCompleted` {#GiveawayCompleted}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **winner\_count** (_int_)

  - **unclaimed\_prize\_count** (_Optional\[int\]_)

  - **giveaway\_message** (_Optional\[Message\]_)

  - **is\_star\_giveaway** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `VideoChatScheduled` {#VideoChatScheduled}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **start\_date** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `VideoChatStarted` {#VideoChatStarted}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `VideoChatEnded` {#VideoChatEnded}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **duration** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `VideoChatParticipantsInvited` {#VideoChatParticipantsInvited}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **users** (_list\[alicebot.adapter.telegram.model.User\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `WebAppData` {#WebAppData}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **data** (_str_)

  - **button\_text** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `WebAppInfo` {#WebAppInfo}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **url** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `LoginUrl` {#LoginUrl}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **url** (_str_)

  - **forward\_text** (_Optional\[str\]_)

  - **bot\_username** (_Optional\[str\]_)

  - **request\_write\_access** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `SwitchInlineQueryChosenChat` {#SwitchInlineQueryChosenChat}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **query** (_Optional\[str\]_)

  - **allow\_user\_chats** (_Optional\[bool\]_)

  - **allow\_bot\_chats** (_Optional\[bool\]_)

  - **allow\_group\_chats** (_Optional\[bool\]_)

  - **allow\_channel\_chats** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `CallbackGame` {#CallbackGame}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineKeyboardButton` {#InlineKeyboardButton}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **text** (_str_)

  - **url** (_Optional\[str\]_)

  - **callback\_data** (_Optional\[str\]_)

  - **web\_app** (_Optional\[alicebot.adapter.telegram.model.WebAppInfo\]_)

  - **login\_url** (_Optional\[alicebot.adapter.telegram.model.LoginUrl\]_)

  - **switch\_inline\_query** (_Optional\[str\]_)

  - **switch\_inline\_query\_current\_chat** (_Optional\[str\]_)

  - **switch\_inline\_query\_chosen\_chat** (_Optional\[alicebot.adapter.telegram.model.SwitchInlineQueryChosenChat\]_)

  - **callback\_game** (_Optional\[alicebot.adapter.telegram.model.CallbackGame\]_)

  - **pay** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineKeyboardMarkup` {#InlineKeyboardMarkup}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **inline\_keyboard** (_list\[list\[alicebot.adapter.telegram.model.InlineKeyboardButton\]\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Message` {#Message}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **message\_id** (_int_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **from\_** (_Optional\[alicebot.adapter.telegram.model.User\]_)

  - **sender\_chat** (_Optional\[alicebot.adapter.telegram.model.Chat\]_)

  - **sender\_boost\_count** (_Optional\[int\]_)

  - **sender\_business\_bot** (_Optional\[alicebot.adapter.telegram.model.User\]_)

  - **date** (_int_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **chat** (_Chat_)

  - **forward\_origin** (_Union\[alicebot.adapter.telegram.model.MessageOriginUser, alicebot.adapter.telegram.model.MessageOriginHiddenUser, alicebot.adapter.telegram.model.MessageOriginChat, alicebot.adapter.telegram.model.MessageOriginChannel, NoneType\]_)

  - **is\_topic\_message** (_Optional\[bool\]_)

  - **is\_automatic\_forward** (_Optional\[bool\]_)

  - **reply\_to\_message** (_Optional\[Message\]_)

  - **external\_reply** (_Optional\[alicebot.adapter.telegram.model.ExternalReplyInfo\]_)

  - **quote** (_Optional\[alicebot.adapter.telegram.model.TextQuote\]_)

  - **reply\_to\_story** (_Optional\[alicebot.adapter.telegram.model.Story\]_)

  - **via\_bot** (_Optional\[alicebot.adapter.telegram.model.User\]_)

  - **edit\_date** (_Optional\[int\]_)

  - **has\_protected\_content** (_Optional\[bool\]_)

  - **is\_from\_offline** (_Optional\[bool\]_)

  - **media\_group\_id** (_Optional\[str\]_)

  - **author\_signature** (_Optional\[str\]_)

  - **text** (_Optional\[str\]_)

  - **entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **link\_preview\_options** (_Optional\[alicebot.adapter.telegram.model.LinkPreviewOptions\]_)

  - **effect\_id** (_Optional\[str\]_)

  - **animation** (_Optional\[alicebot.adapter.telegram.model.Animation\]_)

  - **audio** (_Optional\[alicebot.adapter.telegram.model.Audio\]_)

  - **document** (_Optional\[alicebot.adapter.telegram.model.Document\]_)

  - **paid\_media** (_Optional\[alicebot.adapter.telegram.model.PaidMediaInfo\]_)

  - **photo** (_Optional\[list\[alicebot.adapter.telegram.model.PhotoSize\]\]_)

  - **sticker** (_Optional\[alicebot.adapter.telegram.model.Sticker\]_)

  - **story** (_Optional\[alicebot.adapter.telegram.model.Story\]_)

  - **video** (_Optional\[alicebot.adapter.telegram.model.Video\]_)

  - **video\_note** (_Optional\[alicebot.adapter.telegram.model.VideoNote\]_)

  - **voice** (_Optional\[alicebot.adapter.telegram.model.Voice\]_)

  - **caption** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **has\_media\_spoiler** (_Optional\[bool\]_)

  - **contact** (_Optional\[alicebot.adapter.telegram.model.Contact\]_)

  - **dice** (_Optional\[alicebot.adapter.telegram.model.Dice\]_)

  - **game** (_Optional\[alicebot.adapter.telegram.model.Game\]_)

  - **poll** (_Optional\[alicebot.adapter.telegram.model.Poll\]_)

  - **venue** (_Optional\[alicebot.adapter.telegram.model.Venue\]_)

  - **location** (_Optional\[alicebot.adapter.telegram.model.Location\]_)

  - **new\_chat\_members** (_Optional\[list\[alicebot.adapter.telegram.model.User\]\]_)

  - **left\_chat\_member** (_Optional\[alicebot.adapter.telegram.model.User\]_)

  - **new\_chat\_title** (_Optional\[str\]_)

  - **new\_chat\_photo** (_Optional\[list\[alicebot.adapter.telegram.model.PhotoSize\]\]_)

  - **delete\_chat\_photo** (_Optional\[bool\]_)

  - **group\_chat\_created** (_Optional\[bool\]_)

  - **supergroup\_chat\_created** (_Optional\[bool\]_)

  - **channel\_chat\_created** (_Optional\[bool\]_)

  - **message\_auto\_delete\_timer\_changed** (_Optional\[alicebot.adapter.telegram.model.MessageAutoDeleteTimerChanged\]_)

  - **migrate\_to\_chat\_id** (_Optional\[int\]_)

  - **migrate\_from\_chat\_id** (_Optional\[int\]_)

  - **pinned\_message** (_Union\[Message, alicebot.adapter.telegram.model.InaccessibleMessage, NoneType\]_)

  - **invoice** (_Optional\[alicebot.adapter.telegram.model.Invoice\]_)

  - **successful\_payment** (_Optional\[alicebot.adapter.telegram.model.SuccessfulPayment\]_)

  - **refunded\_payment** (_Optional\[alicebot.adapter.telegram.model.RefundedPayment\]_)

  - **users\_shared** (_Optional\[alicebot.adapter.telegram.model.UsersShared\]_)

  - **chat\_shared** (_Optional\[alicebot.adapter.telegram.model.ChatShared\]_)

  - **connected\_website** (_Optional\[str\]_)

  - **write\_access\_allowed** (_Optional\[alicebot.adapter.telegram.model.WriteAccessAllowed\]_)

  - **passport\_data** (_Optional\[alicebot.adapter.telegram.model.PassportData\]_)

  - **proximity\_alert\_triggered** (_Optional\[alicebot.adapter.telegram.model.ProximityAlertTriggered\]_)

  - **boost\_added** (_Optional\[alicebot.adapter.telegram.model.ChatBoostAdded\]_)

  - **chat\_background\_set** (_Optional\[alicebot.adapter.telegram.model.ChatBackground\]_)

  - **forum\_topic\_created** (_Optional\[alicebot.adapter.telegram.model.ForumTopicCreated\]_)

  - **forum\_topic\_edited** (_Optional\[alicebot.adapter.telegram.model.ForumTopicEdited\]_)

  - **forum\_topic\_closed** (_Optional\[alicebot.adapter.telegram.model.ForumTopicClosed\]_)

  - **forum\_topic\_reopened** (_Optional\[alicebot.adapter.telegram.model.ForumTopicReopened\]_)

  - **general\_forum\_topic\_hidden** (_Optional\[alicebot.adapter.telegram.model.GeneralForumTopicHidden\]_)

  - **general\_forum\_topic\_unhidden** (_Optional\[alicebot.adapter.telegram.model.GeneralForumTopicUnhidden\]_)

  - **giveaway\_created** (_Optional\[alicebot.adapter.telegram.model.GiveawayCreated\]_)

  - **giveaway** (_Optional\[alicebot.adapter.telegram.model.Giveaway\]_)

  - **giveaway\_winners** (_Optional\[alicebot.adapter.telegram.model.GiveawayWinners\]_)

  - **giveaway\_completed** (_Optional\[alicebot.adapter.telegram.model.GiveawayCompleted\]_)

  - **video\_chat\_scheduled** (_Optional\[alicebot.adapter.telegram.model.VideoChatScheduled\]_)

  - **video\_chat\_started** (_Optional\[alicebot.adapter.telegram.model.VideoChatStarted\]_)

  - **video\_chat\_ended** (_Optional\[alicebot.adapter.telegram.model.VideoChatEnded\]_)

  - **video\_chat\_participants\_invited** (_Optional\[alicebot.adapter.telegram.model.VideoChatParticipantsInvited\]_)

  - **web\_app\_data** (_Optional\[alicebot.adapter.telegram.model.WebAppData\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BusinessConnection` {#BusinessConnection}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **id** (_str_)

  - **user** (_User_)

  - **user\_chat\_id** (_int_)

  - **date** (_int_)

  - **can\_reply** (_bool_)

  - **is\_enabled** (_bool_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BusinessMessagesDeleted` {#BusinessMessagesDeleted}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **business\_connection\_id** (_str_)

  - **chat** (_Chat_)

  - **message\_ids** (_list\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ReactionTypeEmoji` {#ReactionTypeEmoji}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **emoji** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ReactionTypeCustomEmoji` {#ReactionTypeCustomEmoji}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **custom\_emoji\_id** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ReactionTypePaid` {#ReactionTypePaid}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MessageReactionUpdated` {#MessageReactionUpdated}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **chat** (_Chat_)

  - **message\_id** (_int_)

  - **user** (_Optional\[alicebot.adapter.telegram.model.User\]_)

  - **actor\_chat** (_Optional\[alicebot.adapter.telegram.model.Chat\]_)

  - **date** (_int_)

  - **old\_reaction** (_list\[typing.Union\[alicebot.adapter.telegram.model.ReactionTypeEmoji, alicebot.adapter.telegram.model.ReactionTypeCustomEmoji, alicebot.adapter.telegram.model.ReactionTypePaid\]\]_)

  - **new\_reaction** (_list\[typing.Union\[alicebot.adapter.telegram.model.ReactionTypeEmoji, alicebot.adapter.telegram.model.ReactionTypeCustomEmoji, alicebot.adapter.telegram.model.ReactionTypePaid\]\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ReactionCount` {#ReactionCount}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_Union\[alicebot.adapter.telegram.model.ReactionTypeEmoji, alicebot.adapter.telegram.model.ReactionTypeCustomEmoji, alicebot.adapter.telegram.model.ReactionTypePaid\]_)

  - **total\_count** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MessageReactionCountUpdated` {#MessageReactionCountUpdated}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **chat** (_Chat_)

  - **message\_id** (_int_)

  - **date** (_int_)

  - **reactions** (_list\[alicebot.adapter.telegram.model.ReactionCount\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQuery` {#InlineQuery}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **id** (_str_)

  - **from\_** (_User_)

  - **query** (_str_)

  - **offset** (_str_)

  - **chat\_type** (_Optional\[str\]_)

  - **location** (_Optional\[alicebot.adapter.telegram.model.Location\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChosenInlineResult` {#ChosenInlineResult}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **result\_id** (_str_)

  - **from\_** (_User_)

  - **location** (_Optional\[alicebot.adapter.telegram.model.Location\]_)

  - **inline\_message\_id** (_Optional\[str\]_)

  - **query** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `CallbackQuery` {#CallbackQuery}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **id** (_str_)

  - **from\_** (_User_)

  - **message** (_Union\[Message, alicebot.adapter.telegram.model.InaccessibleMessage, NoneType\]_)

  - **inline\_message\_id** (_Optional\[str\]_)

  - **chat\_instance** (_str_)

  - **data** (_Optional\[str\]_)

  - **game\_short\_name** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ShippingQuery` {#ShippingQuery}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **id** (_str_)

  - **from\_** (_User_)

  - **invoice\_payload** (_str_)

  - **shipping\_address** (_ShippingAddress_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PreCheckoutQuery` {#PreCheckoutQuery}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **id** (_str_)

  - **from\_** (_User_)

  - **currency** (_str_)

  - **total\_amount** (_int_)

  - **invoice\_payload** (_str_)

  - **shipping\_option\_id** (_Optional\[str\]_)

  - **order\_info** (_Optional\[alicebot.adapter.telegram.model.OrderInfo\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PaidMediaPurchased` {#PaidMediaPurchased}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **from\_** (_User_)

  - **paid\_media\_payload** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PollAnswer` {#PollAnswer}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **poll\_id** (_str_)

  - **voter\_chat** (_Optional\[alicebot.adapter.telegram.model.Chat\]_)

  - **user** (_Optional\[alicebot.adapter.telegram.model.User\]_)

  - **option\_ids** (_list\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatMemberOwner` {#ChatMemberOwner}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **status** (_str_)

  - **user** (_User_)

  - **is\_anonymous** (_bool_)

  - **custom\_title** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatMemberAdministrator` {#ChatMemberAdministrator}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **status** (_str_)

  - **user** (_User_)

  - **can\_be\_edited** (_bool_)

  - **is\_anonymous** (_bool_)

  - **can\_manage\_chat** (_bool_)

  - **can\_delete\_messages** (_bool_)

  - **can\_manage\_video\_chats** (_bool_)

  - **can\_restrict\_members** (_bool_)

  - **can\_promote\_members** (_bool_)

  - **can\_change\_info** (_bool_)

  - **can\_invite\_users** (_bool_)

  - **can\_post\_stories** (_bool_)

  - **can\_edit\_stories** (_bool_)

  - **can\_delete\_stories** (_bool_)

  - **can\_post\_messages** (_Optional\[bool\]_)

  - **can\_edit\_messages** (_Optional\[bool\]_)

  - **can\_pin\_messages** (_Optional\[bool\]_)

  - **can\_manage\_topics** (_Optional\[bool\]_)

  - **custom\_title** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatMemberMember` {#ChatMemberMember}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **status** (_str_)

  - **user** (_User_)

  - **until\_date** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatMemberRestricted` {#ChatMemberRestricted}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **status** (_str_)

  - **user** (_User_)

  - **is\_member** (_bool_)

  - **can\_send\_messages** (_bool_)

  - **can\_send\_audios** (_bool_)

  - **can\_send\_documents** (_bool_)

  - **can\_send\_photos** (_bool_)

  - **can\_send\_videos** (_bool_)

  - **can\_send\_video\_notes** (_bool_)

  - **can\_send\_voice\_notes** (_bool_)

  - **can\_send\_polls** (_bool_)

  - **can\_send\_other\_messages** (_bool_)

  - **can\_add\_web\_page\_previews** (_bool_)

  - **can\_change\_info** (_bool_)

  - **can\_invite\_users** (_bool_)

  - **can\_pin\_messages** (_bool_)

  - **can\_manage\_topics** (_bool_)

  - **until\_date** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatMemberLeft` {#ChatMemberLeft}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **status** (_str_)

  - **user** (_User_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatMemberBanned` {#ChatMemberBanned}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **status** (_str_)

  - **user** (_User_)

  - **until\_date** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatInviteLink` {#ChatInviteLink}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **invite\_link** (_str_)

  - **creator** (_User_)

  - **creates\_join\_request** (_bool_)

  - **is\_primary** (_bool_)

  - **is\_revoked** (_bool_)

  - **name** (_Optional\[str\]_)

  - **expire\_date** (_Optional\[int\]_)

  - **member\_limit** (_Optional\[int\]_)

  - **pending\_join\_request\_count** (_Optional\[int\]_)

  - **subscription\_period** (_Optional\[int\]_)

  - **subscription\_price** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatMemberUpdated` {#ChatMemberUpdated}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **chat** (_Chat_)

  - **from\_** (_User_)

  - **date** (_int_)

  - **old\_chat\_member** (_Union\[alicebot.adapter.telegram.model.ChatMemberOwner, alicebot.adapter.telegram.model.ChatMemberAdministrator, alicebot.adapter.telegram.model.ChatMemberMember, alicebot.adapter.telegram.model.ChatMemberRestricted, alicebot.adapter.telegram.model.ChatMemberLeft, alicebot.adapter.telegram.model.ChatMemberBanned\]_)

  - **new\_chat\_member** (_Union\[alicebot.adapter.telegram.model.ChatMemberOwner, alicebot.adapter.telegram.model.ChatMemberAdministrator, alicebot.adapter.telegram.model.ChatMemberMember, alicebot.adapter.telegram.model.ChatMemberRestricted, alicebot.adapter.telegram.model.ChatMemberLeft, alicebot.adapter.telegram.model.ChatMemberBanned\]_)

  - **invite\_link** (_Optional\[alicebot.adapter.telegram.model.ChatInviteLink\]_)

  - **via\_join\_request** (_Optional\[bool\]_)

  - **via\_chat\_folder\_invite\_link** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatJoinRequest` {#ChatJoinRequest}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **chat** (_Chat_)

  - **from\_** (_User_)

  - **user\_chat\_id** (_int_)

  - **date** (_int_)

  - **bio** (_Optional\[str\]_)

  - **invite\_link** (_Optional\[alicebot.adapter.telegram.model.ChatInviteLink\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatBoostSourcePremium` {#ChatBoostSourcePremium}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **source** (_str_)

  - **user** (_User_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatBoostSourceGiftCode` {#ChatBoostSourceGiftCode}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **source** (_str_)

  - **user** (_User_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatBoostSourceGiveaway` {#ChatBoostSourceGiveaway}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **source** (_str_)

  - **giveaway\_message\_id** (_int_)

  - **user** (_Optional\[alicebot.adapter.telegram.model.User\]_)

  - **prize\_star\_count** (_Optional\[int\]_)

  - **is\_unclaimed** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatBoost` {#ChatBoost}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **boost\_id** (_str_)

  - **add\_date** (_int_)

  - **expiration\_date** (_int_)

  - **source** (_Union\[alicebot.adapter.telegram.model.ChatBoostSourcePremium, alicebot.adapter.telegram.model.ChatBoostSourceGiftCode, alicebot.adapter.telegram.model.ChatBoostSourceGiveaway\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatBoostUpdated` {#ChatBoostUpdated}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **chat** (_Chat_)

  - **boost** (_ChatBoost_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatBoostRemoved` {#ChatBoostRemoved}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **chat** (_Chat_)

  - **boost\_id** (_str_)

  - **remove\_date** (_int_)

  - **source** (_Union\[alicebot.adapter.telegram.model.ChatBoostSourcePremium, alicebot.adapter.telegram.model.ChatBoostSourceGiftCode, alicebot.adapter.telegram.model.ChatBoostSourceGiveaway\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Update` {#Update}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **update\_id** (_int_)

  - **message** (_Optional\[alicebot.adapter.telegram.model.Message\]_)

  - **edited\_message** (_Optional\[alicebot.adapter.telegram.model.Message\]_)

  - **channel\_post** (_Optional\[alicebot.adapter.telegram.model.Message\]_)

  - **edited\_channel\_post** (_Optional\[alicebot.adapter.telegram.model.Message\]_)

  - **business\_connection** (_Optional\[alicebot.adapter.telegram.model.BusinessConnection\]_)

  - **business\_message** (_Optional\[alicebot.adapter.telegram.model.Message\]_)

  - **edited\_business\_message** (_Optional\[alicebot.adapter.telegram.model.Message\]_)

  - **deleted\_business\_messages** (_Optional\[alicebot.adapter.telegram.model.BusinessMessagesDeleted\]_)

  - **message\_reaction** (_Optional\[alicebot.adapter.telegram.model.MessageReactionUpdated\]_)

  - **message\_reaction\_count** (_Optional\[alicebot.adapter.telegram.model.MessageReactionCountUpdated\]_)

  - **inline\_query** (_Optional\[alicebot.adapter.telegram.model.InlineQuery\]_)

  - **chosen\_inline\_result** (_Optional\[alicebot.adapter.telegram.model.ChosenInlineResult\]_)

  - **callback\_query** (_Optional\[alicebot.adapter.telegram.model.CallbackQuery\]_)

  - **shipping\_query** (_Optional\[alicebot.adapter.telegram.model.ShippingQuery\]_)

  - **pre\_checkout\_query** (_Optional\[alicebot.adapter.telegram.model.PreCheckoutQuery\]_)

  - **purchased\_paid\_media** (_Optional\[alicebot.adapter.telegram.model.PaidMediaPurchased\]_)

  - **poll** (_Optional\[alicebot.adapter.telegram.model.Poll\]_)

  - **poll\_answer** (_Optional\[alicebot.adapter.telegram.model.PollAnswer\]_)

  - **my\_chat\_member** (_Optional\[alicebot.adapter.telegram.model.ChatMemberUpdated\]_)

  - **chat\_member** (_Optional\[alicebot.adapter.telegram.model.ChatMemberUpdated\]_)

  - **chat\_join\_request** (_Optional\[alicebot.adapter.telegram.model.ChatJoinRequest\]_)

  - **chat\_boost** (_Optional\[alicebot.adapter.telegram.model.ChatBoostUpdated\]_)

  - **removed\_chat\_boost** (_Optional\[alicebot.adapter.telegram.model.ChatBoostRemoved\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `WebhookInfo` {#WebhookInfo}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **url** (_str_)

  - **has\_custom\_certificate** (_bool_)

  - **pending\_update\_count** (_int_)

  - **ip\_address** (_Optional\[str\]_)

  - **last\_error\_date** (_Optional\[int\]_)

  - **last\_error\_message** (_Optional\[str\]_)

  - **last\_synchronization\_error\_date** (_Optional\[int\]_)

  - **max\_connections** (_Optional\[int\]_)

  - **allowed\_updates** (_Optional\[list\[str\]\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatPhoto` {#ChatPhoto}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **small\_file\_id** (_str_)

  - **small\_file\_unique\_id** (_str_)

  - **big\_file\_id** (_str_)

  - **big\_file\_unique\_id** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `Birthdate` {#Birthdate}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **day** (_int_)

  - **month** (_int_)

  - **year** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BusinessIntro` {#BusinessIntro}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **title** (_Optional\[str\]_)

  - **message** (_Optional\[str\]_)

  - **sticker** (_Optional\[alicebot.adapter.telegram.model.Sticker\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BusinessLocation` {#BusinessLocation}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **address** (_str_)

  - **location** (_Optional\[alicebot.adapter.telegram.model.Location\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BusinessOpeningHoursInterval` {#BusinessOpeningHoursInterval}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **opening\_minute** (_int_)

  - **closing\_minute** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BusinessOpeningHours` {#BusinessOpeningHours}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **time\_zone\_name** (_str_)

  - **opening\_hours** (_list\[alicebot.adapter.telegram.model.BusinessOpeningHoursInterval\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatPermissions` {#ChatPermissions}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **can\_send\_messages** (_Optional\[bool\]_)

  - **can\_send\_audios** (_Optional\[bool\]_)

  - **can\_send\_documents** (_Optional\[bool\]_)

  - **can\_send\_photos** (_Optional\[bool\]_)

  - **can\_send\_videos** (_Optional\[bool\]_)

  - **can\_send\_video\_notes** (_Optional\[bool\]_)

  - **can\_send\_voice\_notes** (_Optional\[bool\]_)

  - **can\_send\_polls** (_Optional\[bool\]_)

  - **can\_send\_other\_messages** (_Optional\[bool\]_)

  - **can\_add\_web\_page\_previews** (_Optional\[bool\]_)

  - **can\_change\_info** (_Optional\[bool\]_)

  - **can\_invite\_users** (_Optional\[bool\]_)

  - **can\_pin\_messages** (_Optional\[bool\]_)

  - **can\_manage\_topics** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatLocation` {#ChatLocation}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **location** (_Location_)

  - **address** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatFullInfo` {#ChatFullInfo}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **id** (_int_)

  - **type** (_str_)

  - **title** (_Optional\[str\]_)

  - **username** (_Optional\[str\]_)

  - **first\_name** (_Optional\[str\]_)

  - **last\_name** (_Optional\[str\]_)

  - **is\_forum** (_Optional\[bool\]_)

  - **accent\_color\_id** (_int_)

  - **max\_reaction\_count** (_int_)

  - **photo** (_Optional\[alicebot.adapter.telegram.model.ChatPhoto\]_)

  - **active\_usernames** (_Optional\[list\[str\]\]_)

  - **birthdate** (_Optional\[alicebot.adapter.telegram.model.Birthdate\]_)

  - **business\_intro** (_Optional\[alicebot.adapter.telegram.model.BusinessIntro\]_)

  - **business\_location** (_Optional\[alicebot.adapter.telegram.model.BusinessLocation\]_)

  - **business\_opening\_hours** (_Optional\[alicebot.adapter.telegram.model.BusinessOpeningHours\]_)

  - **personal\_chat** (_Optional\[alicebot.adapter.telegram.model.Chat\]_)

  - **available\_reactions** (_Optional\[list\[Union\[alicebot.adapter.telegram.model.ReactionTypeEmoji, alicebot.adapter.telegram.model.ReactionTypeCustomEmoji, alicebot.adapter.telegram.model.ReactionTypePaid\]\]\]_)

  - **background\_custom\_emoji\_id** (_Optional\[str\]_)

  - **profile\_accent\_color\_id** (_Optional\[int\]_)

  - **profile\_background\_custom\_emoji\_id** (_Optional\[str\]_)

  - **emoji\_status\_custom\_emoji\_id** (_Optional\[str\]_)

  - **emoji\_status\_expiration\_date** (_Optional\[int\]_)

  - **bio** (_Optional\[str\]_)

  - **has\_private\_forwards** (_Optional\[bool\]_)

  - **has\_restricted\_voice\_and\_video\_messages** (_Optional\[bool\]_)

  - **join\_to\_send\_messages** (_Optional\[bool\]_)

  - **join\_by\_request** (_Optional\[bool\]_)

  - **description** (_Optional\[str\]_)

  - **invite\_link** (_Optional\[str\]_)

  - **pinned\_message** (_Optional\[alicebot.adapter.telegram.model.Message\]_)

  - **permissions** (_Optional\[alicebot.adapter.telegram.model.ChatPermissions\]_)

  - **can\_send\_paid\_media** (_Optional\[bool\]_)

  - **slow\_mode\_delay** (_Optional\[int\]_)

  - **unrestrict\_boost\_count** (_Optional\[int\]_)

  - **message\_auto\_delete\_time** (_Optional\[int\]_)

  - **has\_aggressive\_anti\_spam\_enabled** (_Optional\[bool\]_)

  - **has\_hidden\_members** (_Optional\[bool\]_)

  - **has\_protected\_content** (_Optional\[bool\]_)

  - **has\_visible\_history** (_Optional\[bool\]_)

  - **sticker\_set\_name** (_Optional\[str\]_)

  - **can\_set\_sticker\_set** (_Optional\[bool\]_)

  - **custom\_emoji\_sticker\_set\_name** (_Optional\[str\]_)

  - **linked\_chat\_id** (_Optional\[int\]_)

  - **location** (_Optional\[alicebot.adapter.telegram.model.ChatLocation\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MessageId` {#MessageId}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **message\_id** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ReplyParameters` {#ReplyParameters}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **message\_id** (_int_)

  - **chat\_id** (_Union\[int, str, NoneType\]_)

  - **allow\_sending\_without\_reply** (_Optional\[bool\]_)

  - **quote** (_Optional\[str\]_)

  - **quote\_parse\_mode** (_Optional\[str\]_)

  - **quote\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **quote\_position** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputPollOption` {#InputPollOption}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **text** (_str_)

  - **text\_parse\_mode** (_Optional\[str\]_)

  - **text\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `UserProfilePhotos` {#UserProfilePhotos}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **total\_count** (_int_)

  - **photos** (_list\[list\[alicebot.adapter.telegram.model.PhotoSize\]\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `KeyboardButtonRequestUsers` {#KeyboardButtonRequestUsers}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **request\_id** (_int_)

  - **user\_is\_bot** (_Optional\[bool\]_)

  - **user\_is\_premium** (_Optional\[bool\]_)

  - **max\_quantity** (_Optional\[int\]_)

  - **request\_name** (_Optional\[bool\]_)

  - **request\_username** (_Optional\[bool\]_)

  - **request\_photo** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ChatAdministratorRights` {#ChatAdministratorRights}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **is\_anonymous** (_bool_)

  - **can\_manage\_chat** (_bool_)

  - **can\_delete\_messages** (_bool_)

  - **can\_manage\_video\_chats** (_bool_)

  - **can\_restrict\_members** (_bool_)

  - **can\_promote\_members** (_bool_)

  - **can\_change\_info** (_bool_)

  - **can\_invite\_users** (_bool_)

  - **can\_post\_stories** (_bool_)

  - **can\_edit\_stories** (_bool_)

  - **can\_delete\_stories** (_bool_)

  - **can\_post\_messages** (_Optional\[bool\]_)

  - **can\_edit\_messages** (_Optional\[bool\]_)

  - **can\_pin\_messages** (_Optional\[bool\]_)

  - **can\_manage\_topics** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `KeyboardButtonRequestChat` {#KeyboardButtonRequestChat}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **request\_id** (_int_)

  - **chat\_is\_channel** (_bool_)

  - **chat\_is\_forum** (_Optional\[bool\]_)

  - **chat\_has\_username** (_Optional\[bool\]_)

  - **chat\_is\_created** (_Optional\[bool\]_)

  - **user\_administrator\_rights** (_Optional\[alicebot.adapter.telegram.model.ChatAdministratorRights\]_)

  - **bot\_administrator\_rights** (_Optional\[alicebot.adapter.telegram.model.ChatAdministratorRights\]_)

  - **bot\_is\_member** (_Optional\[bool\]_)

  - **request\_title** (_Optional\[bool\]_)

  - **request\_username** (_Optional\[bool\]_)

  - **request\_photo** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `KeyboardButtonPollType` {#KeyboardButtonPollType}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `KeyboardButton` {#KeyboardButton}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **text** (_str_)

  - **request\_users** (_Optional\[alicebot.adapter.telegram.model.KeyboardButtonRequestUsers\]_)

  - **request\_chat** (_Optional\[alicebot.adapter.telegram.model.KeyboardButtonRequestChat\]_)

  - **request\_contact** (_Optional\[bool\]_)

  - **request\_location** (_Optional\[bool\]_)

  - **request\_poll** (_Optional\[alicebot.adapter.telegram.model.KeyboardButtonPollType\]_)

  - **web\_app** (_Optional\[alicebot.adapter.telegram.model.WebAppInfo\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ReplyKeyboardMarkup` {#ReplyKeyboardMarkup}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **keyboard** (_list\[list\[alicebot.adapter.telegram.model.KeyboardButton\]\]_)

  - **is\_persistent** (_Optional\[bool\]_)

  - **resize\_keyboard** (_Optional\[bool\]_)

  - **one\_time\_keyboard** (_Optional\[bool\]_)

  - **input\_field\_placeholder** (_Optional\[str\]_)

  - **selective** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ReplyKeyboardRemove` {#ReplyKeyboardRemove}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **remove\_keyboard** (_bool_)

  - **selective** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ForceReply` {#ForceReply}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **force\_reply** (_bool_)

  - **input\_field\_placeholder** (_Optional\[str\]_)

  - **selective** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ForumTopic` {#ForumTopic}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **message\_thread\_id** (_int_)

  - **name** (_str_)

  - **icon\_color** (_int_)

  - **icon\_custom\_emoji\_id** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BotCommand` {#BotCommand}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **command** (_str_)

  - **description** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BotCommandScopeDefault` {#BotCommandScopeDefault}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BotCommandScopeAllPrivateChats` {#BotCommandScopeAllPrivateChats}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BotCommandScopeAllGroupChats` {#BotCommandScopeAllGroupChats}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BotCommandScopeAllChatAdministrators` {#BotCommandScopeAllChatAdministrators}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BotCommandScopeChat` {#BotCommandScopeChat}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **chat\_id** (_Union\[int, str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BotCommandScopeChatAdministrators` {#BotCommandScopeChatAdministrators}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **chat\_id** (_Union\[int, str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BotCommandScopeChatMember` {#BotCommandScopeChatMember}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **chat\_id** (_Union\[int, str\]_)

  - **user\_id** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BotName` {#BotName}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **name** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BotDescription` {#BotDescription}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **description** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `BotShortDescription` {#BotShortDescription}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **short\_description** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MenuButtonCommands` {#MenuButtonCommands}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MenuButtonWebApp` {#MenuButtonWebApp}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **text** (_str_)

  - **web\_app** (_WebAppInfo_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `MenuButtonDefault` {#MenuButtonDefault}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `UserChatBoosts` {#UserChatBoosts}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **boosts** (_list\[alicebot.adapter.telegram.model.ChatBoost\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ResponseParameters` {#ResponseParameters}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **migrate\_to\_chat\_id** (_Optional\[int\]_)

  - **retry\_after** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputMediaAnimation` {#InputMediaAnimation}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **media** (_str_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **width** (_Optional\[int\]_)

  - **height** (_Optional\[int\]_)

  - **duration** (_Optional\[int\]_)

  - **has\_spoiler** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputMediaDocument` {#InputMediaDocument}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **media** (_str_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **disable\_content\_type\_detection** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputMediaAudio` {#InputMediaAudio}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **media** (_str_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **duration** (_Optional\[int\]_)

  - **performer** (_Optional\[str\]_)

  - **title** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputMediaPhoto` {#InputMediaPhoto}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **media** (_str_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **has\_spoiler** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputMediaVideo` {#InputMediaVideo}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **media** (_str_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **width** (_Optional\[int\]_)

  - **height** (_Optional\[int\]_)

  - **duration** (_Optional\[int\]_)

  - **supports\_streaming** (_Optional\[bool\]_)

  - **has\_spoiler** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputPaidMediaPhoto` {#InputPaidMediaPhoto}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **media** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputPaidMediaVideo` {#InputPaidMediaVideo}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **media** (_str_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **width** (_Optional\[int\]_)

  - **height** (_Optional\[int\]_)

  - **duration** (_Optional\[int\]_)

  - **supports\_streaming** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `StickerSet` {#StickerSet}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **name** (_str_)

  - **title** (_str_)

  - **sticker\_type** (_str_)

  - **stickers** (_list\[alicebot.adapter.telegram.model.Sticker\]_)

  - **thumbnail** (_Optional\[alicebot.adapter.telegram.model.PhotoSize\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputSticker` {#InputSticker}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **sticker** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **format** (_str_)

  - **emoji\_list** (_list\[str\]_)

  - **mask\_position** (_Optional\[alicebot.adapter.telegram.model.MaskPosition\]_)

  - **keywords** (_Optional\[list\[str\]\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultsButton` {#InlineQueryResultsButton}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **text** (_str_)

  - **web\_app** (_Optional\[alicebot.adapter.telegram.model.WebAppInfo\]_)

  - **start\_parameter** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputTextMessageContent` {#InputTextMessageContent}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **message\_text** (_str_)

  - **parse\_mode** (_Optional\[str\]_)

  - **entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **link\_preview\_options** (_Optional\[alicebot.adapter.telegram.model.LinkPreviewOptions\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputLocationMessageContent` {#InputLocationMessageContent}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **latitude** (_float_)

  - **longitude** (_float_)

  - **horizontal\_accuracy** (_Optional\[float\]_)

  - **live\_period** (_Optional\[int\]_)

  - **heading** (_Optional\[int\]_)

  - **proximity\_alert\_radius** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputVenueMessageContent` {#InputVenueMessageContent}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **latitude** (_float_)

  - **longitude** (_float_)

  - **title** (_str_)

  - **address** (_str_)

  - **foursquare\_id** (_Optional\[str\]_)

  - **foursquare\_type** (_Optional\[str\]_)

  - **google\_place\_id** (_Optional\[str\]_)

  - **google\_place\_type** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputContactMessageContent` {#InputContactMessageContent}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **phone\_number** (_str_)

  - **first\_name** (_str_)

  - **last\_name** (_Optional\[str\]_)

  - **vcard** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `LabeledPrice` {#LabeledPrice}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **label** (_str_)

  - **amount** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InputInvoiceMessageContent` {#InputInvoiceMessageContent}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **title** (_str_)

  - **description** (_str_)

  - **payload** (_str_)

  - **provider\_token** (_Optional\[str\]_)

  - **currency** (_str_)

  - **prices** (_list\[alicebot.adapter.telegram.model.LabeledPrice\]_)

  - **max\_tip\_amount** (_Optional\[int\]_)

  - **suggested\_tip\_amounts** (_Optional\[list\[int\]\]_)

  - **provider\_data** (_Optional\[str\]_)

  - **photo\_url** (_Optional\[str\]_)

  - **photo\_size** (_Optional\[int\]_)

  - **photo\_width** (_Optional\[int\]_)

  - **photo\_height** (_Optional\[int\]_)

  - **need\_name** (_Optional\[bool\]_)

  - **need\_phone\_number** (_Optional\[bool\]_)

  - **need\_email** (_Optional\[bool\]_)

  - **need\_shipping\_address** (_Optional\[bool\]_)

  - **send\_phone\_number\_to\_provider** (_Optional\[bool\]_)

  - **send\_email\_to\_provider** (_Optional\[bool\]_)

  - **is\_flexible** (_Optional\[bool\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultCachedAudio` {#InlineQueryResultCachedAudio}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **audio\_file\_id** (_str_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultCachedDocument` {#InlineQueryResultCachedDocument}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **title** (_str_)

  - **document\_file\_id** (_str_)

  - **description** (_Optional\[str\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultCachedGif` {#InlineQueryResultCachedGif}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **gif\_file\_id** (_str_)

  - **title** (_Optional\[str\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultCachedMpeg4Gif` {#InlineQueryResultCachedMpeg4Gif}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **mpeg4\_file\_id** (_str_)

  - **title** (_Optional\[str\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultCachedPhoto` {#InlineQueryResultCachedPhoto}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **photo\_file\_id** (_str_)

  - **title** (_Optional\[str\]_)

  - **description** (_Optional\[str\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultCachedSticker` {#InlineQueryResultCachedSticker}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **sticker\_file\_id** (_str_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultCachedVideo` {#InlineQueryResultCachedVideo}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **video\_file\_id** (_str_)

  - **title** (_str_)

  - **description** (_Optional\[str\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultCachedVoice` {#InlineQueryResultCachedVoice}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **voice\_file\_id** (_str_)

  - **title** (_str_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultArticle` {#InlineQueryResultArticle}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **title** (_str_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **url** (_Optional\[str\]_)

  - **hide\_url** (_Optional\[bool\]_)

  - **description** (_Optional\[str\]_)

  - **thumbnail\_url** (_Optional\[str\]_)

  - **thumbnail\_width** (_Optional\[int\]_)

  - **thumbnail\_height** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultAudio` {#InlineQueryResultAudio}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **audio\_url** (_str_)

  - **title** (_str_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **performer** (_Optional\[str\]_)

  - **audio\_duration** (_Optional\[int\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultContact` {#InlineQueryResultContact}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **phone\_number** (_str_)

  - **first\_name** (_str_)

  - **last\_name** (_Optional\[str\]_)

  - **vcard** (_Optional\[str\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **thumbnail\_url** (_Optional\[str\]_)

  - **thumbnail\_width** (_Optional\[int\]_)

  - **thumbnail\_height** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultGame` {#InlineQueryResultGame}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **game\_short\_name** (_str_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultDocument` {#InlineQueryResultDocument}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **title** (_str_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **document\_url** (_str_)

  - **mime\_type** (_str_)

  - **description** (_Optional\[str\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **thumbnail\_url** (_Optional\[str\]_)

  - **thumbnail\_width** (_Optional\[int\]_)

  - **thumbnail\_height** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultGif` {#InlineQueryResultGif}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **gif\_url** (_str_)

  - **gif\_width** (_Optional\[int\]_)

  - **gif\_height** (_Optional\[int\]_)

  - **gif\_duration** (_Optional\[int\]_)

  - **thumbnail\_url** (_str_)

  - **thumbnail\_mime\_type** (_Optional\[str\]_)

  - **title** (_Optional\[str\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultLocation` {#InlineQueryResultLocation}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **latitude** (_float_)

  - **longitude** (_float_)

  - **title** (_str_)

  - **horizontal\_accuracy** (_Optional\[float\]_)

  - **live\_period** (_Optional\[int\]_)

  - **heading** (_Optional\[int\]_)

  - **proximity\_alert\_radius** (_Optional\[int\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **thumbnail\_url** (_Optional\[str\]_)

  - **thumbnail\_width** (_Optional\[int\]_)

  - **thumbnail\_height** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultMpeg4Gif` {#InlineQueryResultMpeg4Gif}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **mpeg4\_url** (_str_)

  - **mpeg4\_width** (_Optional\[int\]_)

  - **mpeg4\_height** (_Optional\[int\]_)

  - **mpeg4\_duration** (_Optional\[int\]_)

  - **thumbnail\_url** (_str_)

  - **thumbnail\_mime\_type** (_Optional\[str\]_)

  - **title** (_Optional\[str\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultPhoto` {#InlineQueryResultPhoto}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **photo\_url** (_str_)

  - **thumbnail\_url** (_str_)

  - **photo\_width** (_Optional\[int\]_)

  - **photo\_height** (_Optional\[int\]_)

  - **title** (_Optional\[str\]_)

  - **description** (_Optional\[str\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultVenue` {#InlineQueryResultVenue}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **latitude** (_float_)

  - **longitude** (_float_)

  - **title** (_str_)

  - **address** (_str_)

  - **foursquare\_id** (_Optional\[str\]_)

  - **foursquare\_type** (_Optional\[str\]_)

  - **google\_place\_id** (_Optional\[str\]_)

  - **google\_place\_type** (_Optional\[str\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **thumbnail\_url** (_Optional\[str\]_)

  - **thumbnail\_width** (_Optional\[int\]_)

  - **thumbnail\_height** (_Optional\[int\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultVideo` {#InlineQueryResultVideo}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **video\_url** (_str_)

  - **mime\_type** (_str_)

  - **thumbnail\_url** (_str_)

  - **title** (_str_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **video\_width** (_Optional\[int\]_)

  - **video\_height** (_Optional\[int\]_)

  - **video\_duration** (_Optional\[int\]_)

  - **description** (_Optional\[str\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `InlineQueryResultVoice` {#InlineQueryResultVoice}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **id** (_str_)

  - **voice\_url** (_str_)

  - **title** (_str_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **voice\_duration** (_Optional\[int\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

  - **input\_message\_content** (_Union\[alicebot.adapter.telegram.model.InputTextMessageContent, alicebot.adapter.telegram.model.InputLocationMessageContent, alicebot.adapter.telegram.model.InputVenueMessageContent, alicebot.adapter.telegram.model.InputContactMessageContent, alicebot.adapter.telegram.model.InputInvoiceMessageContent, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `SentWebAppMessage` {#SentWebAppMessage}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **inline\_message\_id** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `ShippingOption` {#ShippingOption}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **id** (_str_)

  - **title** (_str_)

  - **prices** (_list\[alicebot.adapter.telegram.model.LabeledPrice\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `RevenueWithdrawalStatePending` {#RevenueWithdrawalStatePending}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `RevenueWithdrawalStateSucceeded` {#RevenueWithdrawalStateSucceeded}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **date** (_int_)

  - **url** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `RevenueWithdrawalStateFailed` {#RevenueWithdrawalStateFailed}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `TransactionPartnerUser` {#TransactionPartnerUser}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **user** (_User_)

  - **invoice\_payload** (_Optional\[str\]_)

  - **paid\_media** (_Optional\[list\[Union\[alicebot.adapter.telegram.model.PaidMediaPreview, alicebot.adapter.telegram.model.PaidMediaPhoto, alicebot.adapter.telegram.model.PaidMediaVideo\]\]\]_)

  - **paid\_media\_payload** (_Optional\[str\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `TransactionPartnerFragment` {#TransactionPartnerFragment}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **withdrawal\_state** (_Union\[alicebot.adapter.telegram.model.RevenueWithdrawalStatePending, alicebot.adapter.telegram.model.RevenueWithdrawalStateSucceeded, alicebot.adapter.telegram.model.RevenueWithdrawalStateFailed, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `TransactionPartnerTelegramAds` {#TransactionPartnerTelegramAds}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `TransactionPartnerOther` {#TransactionPartnerOther}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **type** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `StarTransaction` {#StarTransaction}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **id** (_str_)

  - **amount** (_int_)

  - **date** (_int_)

  - **source** (_Union\[alicebot.adapter.telegram.model.TransactionPartnerUser, alicebot.adapter.telegram.model.TransactionPartnerFragment, alicebot.adapter.telegram.model.TransactionPartnerTelegramAds, alicebot.adapter.telegram.model.TransactionPartnerOther, NoneType\]_)

  - **receiver** (_Union\[alicebot.adapter.telegram.model.TransactionPartnerUser, alicebot.adapter.telegram.model.TransactionPartnerFragment, alicebot.adapter.telegram.model.TransactionPartnerTelegramAds, alicebot.adapter.telegram.model.TransactionPartnerOther, NoneType\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `StarTransactions` {#StarTransactions}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **transactions** (_list\[alicebot.adapter.telegram.model.StarTransaction\]_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PassportElementErrorDataField` {#PassportElementErrorDataField}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **source** (_str_)

  - **type** (_str_)

  - **field\_name** (_str_)

  - **data\_hash** (_str_)

  - **message** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PassportElementErrorFrontSide` {#PassportElementErrorFrontSide}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **source** (_str_)

  - **type** (_str_)

  - **file\_hash** (_str_)

  - **message** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PassportElementErrorReverseSide` {#PassportElementErrorReverseSide}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **source** (_str_)

  - **type** (_str_)

  - **file\_hash** (_str_)

  - **message** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PassportElementErrorSelfie` {#PassportElementErrorSelfie}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **source** (_str_)

  - **type** (_str_)

  - **file\_hash** (_str_)

  - **message** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PassportElementErrorFile` {#PassportElementErrorFile}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **source** (_str_)

  - **type** (_str_)

  - **file\_hash** (_str_)

  - **message** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PassportElementErrorFiles` {#PassportElementErrorFiles}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **source** (_str_)

  - **type** (_str_)

  - **file\_hashes** (_list\[str\]_)

  - **message** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PassportElementErrorTranslationFile` {#PassportElementErrorTranslationFile}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **source** (_str_)

  - **type** (_str_)

  - **file\_hash** (_str_)

  - **message** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PassportElementErrorTranslationFiles` {#PassportElementErrorTranslationFiles}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **source** (_str_)

  - **type** (_str_)

  - **file\_hashes** (_list\[str\]_)

  - **message** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `PassportElementErrorUnspecified` {#PassportElementErrorUnspecified}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **source** (_str_)

  - **type** (_str_)

  - **element\_hash** (_str_)

  - **message** (_str_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.

## _class_ `GameHighScore` {#GameHighScore}

Bases: `pydantic.main.BaseModel`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **position** (_int_)

  - **user** (_User_)

  - **score** (_int_)

  - **\_\_class\_vars\_\_** - The names of the class variables defined on the model.

  - **\_\_private\_attributes\_\_** - Metadata about the private attributes of the model.

  - **\_\_signature\_\_** - The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

  - **\_\_pydantic\_complete\_\_** - Whether model building is completed, or if there are still undefined fields.

  - **\_\_pydantic\_core\_schema\_\_** - The core schema of the model.

  - **\_\_pydantic\_custom\_init\_\_** - Whether the model has a custom `__init__` function.

  - **\_\_pydantic\_decorators\_\_** - Metadata containing the decorators defined on the model.
  This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

  - **\_\_pydantic\_generic\_metadata\_\_** - Metadata for generic models; contains data used for a similar purpose to
  __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

  - **\_\_pydantic\_parent\_namespace\_\_** - Parent namespace of the model, used for automatic rebuilding of models.

  - **\_\_pydantic\_post\_init\_\_** - The name of the post-init method for the model, if defined.

  - **\_\_pydantic\_root\_model\_\_** - Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

  - **\_\_pydantic\_serializer\_\_** - The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

  - **\_\_pydantic\_validator\_\_** - The `pydantic-core` `SchemaValidator` used to validate instances of the model.

  - **\_\_pydantic\_extra\_\_** - A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
  is set to `'allow'`.

  - **\_\_pydantic\_fields\_set\_\_** - The names of fields explicitly set during instantiation.

  - **\_\_pydantic\_private\_\_** - Values of private attributes set on the model instance.
