# alicebot.adapter.telegram.media

Telegram Media 模型。

## _class_ `TelegramMedia` {#TelegramMedia}

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

## _class_ `Photo` {#Photo}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **photo** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **caption** (_Union\[NoneType, str, alicebot.adapter.telegram.message.TelegramMessage\]_)

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

## _class_ `Audio` {#Audio}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **audio** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **caption** (_Union\[NoneType, str, alicebot.adapter.telegram.message.TelegramMessage\]_)

  - **duration** (_Optional\[int\]_)

  - **performer** (_Optional\[str\]_)

  - **title** (_Optional\[str\]_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

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

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **document** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **caption** (_Union\[NoneType, str, alicebot.adapter.telegram.message.TelegramMessage\]_)

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

## _class_ `Video` {#Video}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **video** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **duration** (_Optional\[int\]_)

  - **width** (_Optional\[int\]_)

  - **height** (_Optional\[int\]_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **caption** (_Union\[NoneType, str, alicebot.adapter.telegram.message.TelegramMessage\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **has\_spoiler** (_Optional\[bool\]_)

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

## _class_ `Animation` {#Animation}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **animation** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **duration** (_Optional\[int\]_)

  - **width** (_Optional\[int\]_)

  - **height** (_Optional\[int\]_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **caption** (_Union\[NoneType, str, alicebot.adapter.telegram.message.TelegramMessage\]_)

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

## _class_ `Voice` {#Voice}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **voice** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **caption** (_Union\[NoneType, str, alicebot.adapter.telegram.message.TelegramMessage\]_)

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

## _class_ `VideoNote` {#VideoNote}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **video\_note** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **duration** (_Optional\[int\]_)

  - **length** (_Optional\[int\]_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

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

## _class_ `PaidMedia` {#PaidMedia}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **star\_count** (_int_)

  - **media** (_list\[typing.Union\[alicebot.adapter.telegram.model.InputPaidMediaPhoto, alicebot.adapter.telegram.model.InputPaidMediaVideo\]\]_)

  - **payload** (_Optional\[str\]_)

  - **caption** (_Union\[NoneType, str, alicebot.adapter.telegram.message.TelegramMessage\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

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

## _class_ `MediaGroup` {#MediaGroup}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **media** (_Union\[list\[alicebot.adapter.telegram.model.InputMediaAudio\], list\[alicebot.adapter.telegram.model.InputMediaDocument\], list\[alicebot.adapter.telegram.model.InputMediaPhoto\], list\[alicebot.adapter.telegram.model.InputMediaVideo\]\]_)

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

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

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

## _class_ `Venue` {#Venue}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

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

## _class_ `Contact` {#Contact}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

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

## _class_ `Poll` {#Poll}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **question** (_Union\[NoneType, str, alicebot.adapter.telegram.message.TelegramMessage\]_)

  - **options** (_list\[alicebot.adapter.telegram.model.InputPollOption\]_)

  - **is\_anonymous** (_Optional\[bool\]_)

  - **type** (_Optional\[str\]_)

  - **allows\_multiple\_answers** (_Optional\[bool\]_)

  - **correct\_option\_id** (_Optional\[int\]_)

  - **explanation** (_Union\[NoneType, str, alicebot.adapter.telegram.message.TelegramMessage\]_)

  - **open\_period** (_Optional\[int\]_)

  - **close\_date** (_Optional\[int\]_)

  - **is\_closed** (_Optional\[bool\]_)

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

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **emoji** (_Optional\[str\]_)

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

## _class_ `ChatAction` {#ChatAction}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **action** (_str_)

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

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **sticker** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **emoji** (_Optional\[str\]_)

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

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

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

  - **start\_parameter** (_Optional\[str\]_)

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

## _class_ `Game` {#Game}

Bases: `alicebot.adapter.telegram.media.TelegramMedia`

Usage docs: https://docs.pydantic.dev/2.9/concepts/models/

A base class for creating Pydantic models.

- **Attributes**

  - **game\_short\_name** (_str_)

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
