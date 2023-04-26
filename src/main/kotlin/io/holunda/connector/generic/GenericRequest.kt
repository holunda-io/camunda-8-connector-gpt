package io.holunda.connector.generic

import com.fasterxml.jackson.databind.annotation.*
import io.camunda.connector.api.annotation.*
import io.holunda.connector.common.json.*

data class GenericRequest(
    @field:JsonDeserialize(using = RawJsonDeserializer::class)
    val inputJson: String,
    @field:JsonDeserialize(using = RawJsonDeserializer::class)
    val outputFormat: String,
    val taskDescription: String,
    val model: String,

    @Secret
    var apiKey: String
)