using System;
using UnityEngine;
using UnityEngine.Perception.Randomization.Parameters;
using UnityEngine.Perception.Randomization.Randomizers;
using UnityEngine.Perception.Randomization.Samplers;


[Serializable]
[AddComponentMenu("Perception/Randomizer/SunLightRandomizer")]
public class SunLightRandomizer: Randomizer
{
    

    protected override void OnIterationStart()
    {
        //oncelıkle taglara sahıp olan objelerı bulmamız gerekıyor.
        var taggedObjects=tagManager.Query<SunLightRandomizerTag>();
        //sonrasında her ıteratıonda bu objelerı dolasıcaz.
        foreach(var tag in taggedObjects)
        {
            //her tagın ıcınde bır lıght componentı var. bu componentın ıntensıtysını randomlıyoruz.
            var light=tag.GetComponent<Light>();
            light.color = UnityEngine.Random.ColorHSV(0f, 1f, 0f, 0.15f, 0.9f, 1f);            light.intensity=UnityEngine.Random.Range(50000f,130000f);//rastgele deger uretılır.
            light.transform.rotation=Quaternion.Euler(UnityEngine.Random.Range(20f,80f),UnityEngine.Random.Range(0f,360f),0f);//rastgele yon uretılır.
            Debug.Log(light.intensity);
        }
    }
}
