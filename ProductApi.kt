package com.example.ecommerce_comparator
import retrofit2.Response
import retrofit2.http.GET
import retrofit2.http.Query

interface ProductApi {

    @GET("/scraper")
    suspend fun getProducts(@Query("q") q : String) : Response<List<Product>>
}