<script lang="ts">
    import Icon from './Icon.svelte';

    export let icon: string;
    export let icon_size: string;
    export let heading: string;
    export let content: string;
</script>

<div class="mb-12 lg:mb-0">
    <div class="p-4 bg-blue-600 rounded-full shadow-lg inline-block mb-6">
        <Icon icon={icon} size={icon_size} />
    </div>
    <h5 class="text-lg  md:text-xl lg:text-2xl font-bold mb-4">{heading}</h5>
    <p class="text-base  md:text-lg lg:text-xl text-justify text-gray-300 break-words">{content}</p>
</div>

<style lang="postcss">
    
</style>